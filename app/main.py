
import os
import zipfile
import shutil
import subprocess
from tqdm import tqdm
from time import sleep
import sys

from app.utilities.custom_printing import CustomPrinting
from app.utilities.custom_markdown import CustomMarkdown
from app.utilities.validation import validate_config_format
from app.utilities.reporting import generate_md_report, print_report


def log(step_no, text):
    sleep(0.05)
    CustomPrinting.print_yellow(
        f"Step {step_no}: {text}", bold=True,
    )
    sleep(0.05)


def remove_path(path):
    try:
        # If the path is a file or an empty directory
        os.remove(path)
    except PermissionError:
        # Otherwise
        shutil.rmtree(path)


def clear_submission_directory(directory):
    # The format in which moodle provides the submitted files
    for filename in tqdm(list(filter(
        lambda file: not file.endswith("_assignsubmission_file_"),
        os.listdir(directory)
    ))):
        shutil.rmtree(f"{directory}/{filename}")


def run_homework_tests(config):

    validate_config_format(config)

    HW_NUMBER = config.get("HW_NUMBER")
    HW_NUMBER_STR = f"HW{'0' if HW_NUMBER < 10 else ''}{HW_NUMBER}"
    GIVEN_DIRECTORY = f"{HW_NUMBER_STR}/given"
    SUBMISSION_DIRECTORY = f"{HW_NUMBER_STR}/submission"
    PROTOCOL_LOCATION = f"reports/report_{HW_NUMBER_STR}.md"

    GIVEN_FILES = config.get("GIVEN_FILES")
    SUBMISSION_FILES = config.get("SUBMISSION_FILES")
    FILES_TO_COMPILE = config.get("FILES_TO_COMPILE")

    results = {}
    submission_folders = os.listdir(SUBMISSION_DIRECTORY)

    # *************************************************************************
    log(1, "Removing all unwanted files from the submission directory")
    clear_submission_directory(SUBMISSION_DIRECTORY)

    # *************************************************************************
    log(2, "Creating testing directories")

    # Creating renamed testing directories
    for filename in tqdm(os.listdir(SUBMISSION_DIRECTORY)):
        # The format in which moodle provides the submitted files
        if filename.endswith("_assignsubmission_file_"):
            new_filename = filename.split("_")[0].lower().replace(" ", "-")
            shutil.copytree(
                f"{SUBMISSION_DIRECTORY}/{filename}",
                f"{SUBMISSION_DIRECTORY}/{new_filename}"
            )
            results[new_filename] = {}
        else:
            os.remove(SUBMISSION_DIRECTORY + "/" + filename)

    # *************************************************************************
    # Step 2: Actually Testing each submission
    log(3, "Testing each submission")

    for filename in tqdm(results.keys()):

        # *********************************************************************
        # Test 1: Is there exactly one zip-file?

        directory_content = os.listdir(SUBMISSION_DIRECTORY + "/" + filename)
        if len(directory_content) > 1:
            results[filename]["result"] = "Failed"
            results[filename]["message"] = f"Too many zip-files in directory: {directory_content}"
            continue  # Jump to next attendee

        # *********************************************************************
        # Test 2: Does the zip-file contain all the required files?

        # Extract files from zip-files
        student_path = SUBMISSION_DIRECTORY + "/" + filename
        zip_file_path = student_path + "/" + directory_content[0]
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(student_path)

        # If the contents of the folder do not match the requirements, which are:
        # Each students directory now has the zip-file in it and
        actual_files = list(filter(lambda file: any([
            file.endswith(ext) for ext in [".c", ".h", ".zip"]
        ]), os.listdir(student_path)))
        # directory_content is just the zip-file from before
        desired_files = directory_content + SUBMISSION_FILES

        wrong_files_submitted = not all([
            desired_file in actual_files for desired_file in desired_files
        ])

        if wrong_files_submitted:
            results[filename]["result"] = "Failed"
            results[filename]["message"] = f"Wrong files in zip-file:" + \
                f" Desired: {desired_files}, Actual: {actual_files}"
            continue  # Jump to next attendee

        # *********************************************************************
        # Test 3: Does Compilation work as expected?

        # Copy all given files into the students directory to compile them together
        for given_file in GIVEN_FILES:
            source = f"{GIVEN_DIRECTORY}/{given_file}"
            destination = f"{SUBMISSION_DIRECTORY}/{filename}/{given_file}"
            shutil.copyfile(source, destination)

        # Validate the state of the compilation directory
        directory_content = os.listdir(f"{SUBMISSION_DIRECTORY}/{filename}")
        assert(all([
            file in directory_content for file in (SUBMISSION_FILES + GIVEN_FILES)
        ]))

        # Determining the compilation string
        compilation_string = generate_compilation_string(
            f"{SUBMISSION_DIRECTORY}/{filename}", FILES_TO_COMPILE
        )

        # Compiling the file
        process = subprocess.Popen(
            compilation_string,
            shell=True,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE
        )
        output, message = process.communicate()

        if process.returncode != 0:
            results[filename]["result"] = "Failed"
            results[filename]["message"] = f"Did not compile: {message.decode()}"
            results[filename]["input"] = {}

            for file in SUBMISSION_FILES:
                results[filename]["input"][file] = open(
                    f"{SUBMISSION_DIRECTORY}/{filename}/{file}", 'r'
                ).read()

            continue  # Jump to next attendee

        # *********************************************************************
        # Test 4 (Manual): Execute the file and store the generated output

        execution_string = f"./{SUBMISSION_DIRECTORY}/{filename}/program.out"

        # Executing the file
        process = subprocess.Popen(
            execution_string, shell=True,
            stderr=subprocess.PIPE, stdout=subprocess.PIPE
        )
        output, error_message = process.communicate()
        exit_code = process.returncode

        results[filename]["result"] = "Success"
        results[filename]["exit_code"] = exit_code
        results[filename]["output"] = output.decode("utf-8", "replace")
        results[filename]["input"] = {}

        for file in SUBMISSION_FILES:
            results[filename]["input"][file] = open(
                f"{SUBMISSION_DIRECTORY}/{filename}/{file}", 'r'
            ).read()

        # ---------------------------------------------------------------------

    # Removing all files except for the zip-file
    log(4, "Removing test directories")
    clear_submission_directory(SUBMISSION_DIRECTORY)

    # Generating the test protocol as a markdown file
    log(5, "Generating full report in markdown")
    generate_md_report(results, PROTOCOL_LOCATION, HW_NUMBER)

    # Print out a short version of the test protocol
    log(6, "Printing short report to console")
    print_report(results)


def generate_compilation_string(relative_path, files_to_compile):
    compilation_string = "gcc -Wall -Werror -std=c99"
    for file in files_to_compile:
        compilation_string += f" {relative_path}/{file}"
    compilation_string += f" -o {relative_path}/program.out"
    return compilation_string
