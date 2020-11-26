
import os
import shutil
from tqdm import tqdm
from time import sleep

from src.utilities.custom_printing import CustomPrinting
from src.utilities.validation import validate_config_format
from src.utilities.reporting import generate_md_report, print_report
from src.utilities.testing import run_single_submission_test


def log(step_no, text):
    sleep(0.05)
    CustomPrinting.print(
        f"Step {step_no}: {text}",
        color='yellow', bold=True,
    )
    sleep(0.05)


def clear_submission_directory(directory):
    # The format in which moodle provides the submitted files
    for filename in tqdm(list(filter(
        lambda file: not file.endswith("_assignsubmission_file_"),
        os.listdir(directory)
    ))):
        try:
            shutil.rmtree(f"{directory}/{filename}")
        except:
            try:
                os.remove(f"{directory}/{filename}")
            except:
                print("Don't know what is happening")


def run_all_submission_tests(config, print_results=True):

    validate_config_format(config)

    HW_NUMBER = config.get("HW_NUMBER")
    assert(os.path.exists(f"HW{str(HW_NUMBER).zfill(2)}/given"))
    assert(os.path.exists(f"HW{str(HW_NUMBER).zfill(2)}/submissions"))
    os.chdir(f"HW{str(HW_NUMBER).zfill(2)}/submissions")

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
        results[filename] = run_single_submission_test(
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

    if print_results:
        # *********************************************************************
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

    return list(sorted(filenames))
