
import os


def validate_config_format(config):
    assert isinstance(config, dict)

    assert isinstance(config.get("HW_NUMBER"), int)

    GIVEN_FILES = config.get("GIVEN_FILES")
    SUBMISSION_FILES = config.get("SUBMISSION_FILES")
    FILES_TO_COMPILE = config.get("FILES_TO_COMPILE")

    for config_var in [GIVEN_FILES, SUBMISSION_FILES, FILES_TO_COMPILE]:
        assert isinstance(config_var, list), print
        assert all([
            isinstance(file, str) for file in config_var
        ])

    assert(all([
        file in (SUBMISSION_FILES + GIVEN_FILES) for file in FILES_TO_COMPILE
    ]))
