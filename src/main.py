
import os
import shutil
from tqdm import tqdm
from time import sleep

from src.utilities.custom_printer import CustomPrinter
from src.utilities.validator import Validator
from src.utilities.reporting import Reporting
from src.utilities.testing import Testing


class Main:

    @staticmethod
    def run(config, print_results=True, timeout=15, line_numbers=True):

        Validator.config(config)
        Validator.file_system(config)

        os.chdir(f"HW{str(config.get('HW_NUMBER')).zfill(2)}/submissions")

        # *************************************************************************
        Main._log(1, "Removing all unwanted files from the submission directory")
        Main._clear_submission_directory('.')

        # *************************************************************************
        Main._log(2, "Preparing temporary test directories")
        filenames = Main._prepare_test_directories()

        # *************************************************************************
        Main._log(3, "Testing each submission")

        results = {}
        for filename in tqdm(filenames):
            results[filename] = Testing.run(filename, config, timeout=timeout)

        # *************************************************************************
        Main._log(4, "Removing test directories")
        Main._clear_submission_directory('.')
        os.chdir("../../")

        # *************************************************************************
        Main._log(5, "Generating full report in markdown")
        Reporting.generate_markdown(
            results,
            config.get('HW_NUMBER'),
            line_numbers=line_numbers
        )

        # *************************************************************************
        if print_results:
            Main._log(6, "Printing short report to console")
            Reporting.print(results)

    @staticmethod
    def _log(step_no, text):
        sleep(0.05)
        CustomPrinter.print(
            f"Step {step_no}: {text}",
            color='yellow', bold=True,
        )
        sleep(0.05)

    @staticmethod
    def _prepare_test_directories():
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

    @staticmethod
    def _clear_submission_directory(directory):
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
