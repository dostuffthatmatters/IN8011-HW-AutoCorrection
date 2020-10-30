
import os
import importlib
from src.utilities.validation import validate_config_format


def test_configurations():
    configs = list(filter(
        lambda file: file.startswith("config_") and file.endswith(".py"),
        os.listdir("configs/")
    ))
    print(configs)
    for config in configs:
        print(f"IMPORTING {f'configs.{config[:-3]}'}")
        file = importlib.import_module(f"configs.{config[:-3]}")
        validate_config_format(file.config)
