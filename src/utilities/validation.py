
import os


def validate_config_format(config):
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
