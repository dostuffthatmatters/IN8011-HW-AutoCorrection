
import os


class Validator:

    @staticmethod
    def config(config):
        assert isinstance(config, dict)

        assert isinstance(config.get("HW_NUMBER"), int)

        GIVEN_FILES = config.get("GIVEN_FILES")
        SUBMISSION_FILES = config.get("SUBMISSION_FILES")
        COMPILATION_FILES = config.get("COMPILATION_FILES")

        for config_var in [GIVEN_FILES, SUBMISSION_FILES, COMPILATION_FILES]:
            assert isinstance(config_var, list), print
            assert all([
                isinstance(file, str) for file in config_var
            ])

        assert(all([
            file in (SUBMISSION_FILES + GIVEN_FILES) for file in COMPILATION_FILES
        ]))

    @staticmethod
    def file_system(config):
        HW_DIRECTORY = f"HW{str(config.get('HW_NUMBER')).zfill(2)}"
        assert(os.path.exists(f"{HW_DIRECTORY}/given"))
        assert(os.path.exists(f"{HW_DIRECTORY}/submissions"))
        for given_file in config["GIVEN_FILES"]:
            assert(os.path.exists(f"{HW_DIRECTORY}/given/{given_file}"))
