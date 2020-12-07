
import os
import shutil
import zipfile
import subprocess
import time
import platform
from datetime import datetime


class Testing:

    @staticmethod
    def run(filename, config, timeout, execute):
        GIVEN_FILES = config.get("GIVEN_FILES")
        SUBMISSION_FILES = config.get("SUBMISSION_FILES")
        COMPILATION_FILES = config.get("COMPILATION_FILES")

        result = {}

        # *********************************************************************
        # Test 1: Is there exactly one zip-file?

        directory_content = list(
            filter(lambda x: x.endswith(".zip"), os.listdir(f"./{filename}"))
        )
        if len(directory_content) == 0:
            result["result"] = "Failed due to given submission folder"
            result["output"] = f"No zip-files in directory!"
            return result  # Jump to next attendee
        if len(directory_content) > 1:
            result["result"] = "Failed due to file requirements"
            result["output"] = f"Too many zip-files in directory: " + \
                f"{directory_content}"
            return result  # Jump to next attendee

        # *********************************************************************
        # Test 2: Does the zip-file contain all the required files?

        # Extract files from zip-files
        student_path = f"./{filename}"
        zip_file_path = f"./{filename}/{directory_content[0]}"
        try:
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(student_path)
        except:
            result["result"] = "Failed during zip-extraction"
            result["output"] = f"Could not extract files from zip-file"
            return result  # Jump to next attendee

        # If the contents of the folder do not match the requirements, which are:
        # Each students directory now has the zip-file in it and
        actual_files = os.listdir(student_path)

        # directory_content is just the zip-file from before
        desired_files = directory_content + SUBMISSION_FILES

        wrong_files_submitted = not all([
            f in actual_files for f in desired_files
        ])

        if wrong_files_submitted:
            desired_files = list(
                filter(lambda f: f != directory_content[0], desired_files))
            actual_files = list(
                filter(lambda f: f != directory_content[0], actual_files))
            result["result"] = "Failed due to file requirements"
            result["output"] = f"Wrong files in zip-file:" + \
                f" Desired: {desired_files}, Actual: {actual_files}"
            return result  # Jump to next attendee

        # *********************************************************************
        # If all files to be submitted exist: Add these to the result

        result["input"] = {}

        for file in SUBMISSION_FILES:
            for enc in ['utf-8', 'utf-16', 'iso-8859-15']:
                try:
                    result["input"][file] = open(
                        f"./{filename}/{file}", 'r',
                        encoding=enc
                    ).read()
                    break
                except:
                    continue

            if file not in result["input"]:
                result["input"][file] = \
                    "Really weird file encoding ..."

        # *********************************************************************
        # Test 3: Does Compilation work as expected?

        # Copy all given files into the students directory to compile them together
        for given_file in GIVEN_FILES:
            source = f"../given/{given_file}"
            destination = f"./{filename}/{given_file}"
            shutil.copyfile(source, destination)

        # Validate the state of the compilation directory
        directory_content = os.listdir(f"./{filename}")
        assert(all([
            file in directory_content for file in (SUBMISSION_FILES + GIVEN_FILES)
        ]))

        # Compiling the file
        process = subprocess.Popen(
            Testing._get_compilation_string(
                f"./{filename}", COMPILATION_FILES
            ),
            shell=True,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE
        )
        output, message = process.communicate()

        if process.returncode != 0:
            output = f"Did not compile: {message.decode()}"
            while output.endswith('\n'):
                output = output[:-1]

            result["result"] = "Failed during compilation"
            result["output"] = output

            return result  # Jump to next attendee

        # *********************************************************************
        # Test 4 (Manual): Execute the file and store the generated output

        if execute:
            custom_stdin = "stdin.txt" in os.listdir(f"./{filename}")

            if platform.system() == "Windows":
                cmd = f".\\{filename}\\program.out"
                if custom_stdin:
                    cmd += f" < .\\{filename}\\stdin.txt"
            elif platform.system() in ["Darwin", "Linux"]:
                cmd = f"./{filename}/program.out"
                if custom_stdin:
                    cmd += f" < ./{filename}/stdin.txt"
            else:
                raise Exception("Operating System unknown")

            try:
                t1 = datetime.now()
                output = subprocess.check_output(
                    cmd, shell=True, stderr=subprocess.PIPE,
                    timeout=timeout
                )
                result["result"] = "Successful execution (exit code 0)"
                result["output"] = output.decode("utf-8", "replace")
                result["exit_code"] = 0

                td = datetime.now() - t1
                result["execution_time"] = round(
                    td.seconds + (td.microseconds/1_000_000), 3
                )

            except subprocess.CalledProcessError as e:
                # Non Zero Exit code
                result["result"] = f"Failed during execution (exit code {e.returncode})"
                result["exit_code"] = e.returncode
                result["output"] = e.output.decode("utf-8", "replace")
            except subprocess.TimeoutExpired as e:
                # Timeout reached
                result["result"] = "Failed during execution"
                result["exit_code"] = 1
                result["output"] = f"Execution Timeout: Limit = {timeout}s"
        else:
            result["result"] = "Successful compilation"
            result["output"] = "Execution disabled and tmp directories not removed."

        return result

    @staticmethod
    def _get_compilation_string(relative_path, compilation_files):
        cs = "gcc -Wall -Werror -std=c99"
        for file in compilation_files:
            cs += f" {relative_path}/{file}"
        cs += f" -o {relative_path}/program.out"
        return cs
