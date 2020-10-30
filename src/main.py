
import os
import shutil
from tqdm import tqdm
from time import sleep

from src.utilities.custom_printing import CustomPrinting
from src.utilities.validation import validate_config_format
from src.utilities.reporting import generate_md_report, print_report
from src.utilities.testing import test_single_submission


def log(step_no, text):
    sleep(0.05)
    CustomPrinting.print(
        f"Step {step_no}: {text}",
        color='yellow', bold=True,
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


def test_all_submissions(config):

    validate_config_format(config)

    HW_NUMBER = config.get("HW_NUMBER")
    os.chdir(f"HW{'0' if HW_NUMBER < 10 else ''}{HW_NUMBER}/submissions")

    # *************************************************************************
    log(1, "Removing all unwanted files from the submission directory")
    clear_submission_directory('.')

    # *************************************************************************
    log(2, "Preparing temporary test directories")
    filenames = prepare_test_directories()

    # *************************************************************************
    log(3, "Testing each submission")

    results = {}
    for filename in tqdm(filenames):
        results[filename] = test_single_submission(
            filename, config
        )

    # *************************************************************************
    log(4, "Removing test directories")
    clear_submission_directory('.')
    os.chdir("../../")

    # *************************************************************************
    log(5, "Generating full report in markdown")
    generate_md_report(
        results,
        HW_NUMBER
    )

    # *************************************************************************
    log(6, "Printing short report to console")
    print_report(results)


def prepare_test_directories():
    assert(os.getcwd().endswith('/submissions'))
    filenames = []

    # Create renamed testing directories
    for filename in tqdm(os.listdir('.')):
        # The format in which moodle provides the submitted files
        if filename.endswith("_assignsubmission_file_"):
            new_filename = filename.split("_")[0].lower().replace(" ", "-")
            shutil.copytree(
                f"./{filename}",
                f"./{new_filename}"
            )
            filenames.append(new_filename)
        else:
            os.remove(f"./{filename}")

    return filenames
