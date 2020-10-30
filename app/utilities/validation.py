
def validate_config_format(config):
    assert isinstance(config, dict)

    assert isinstance(config.get("HW_NUMBER"), int)

    for config_var in ["GIVEN_FILES", "SUBMISSION_FILES", "FILES_TO_COMPILE"]:
        assert isinstance(config.get(config_var), list)
        assert all([
            isinstance(file, str) for file in config.get(config_var)
        ])
