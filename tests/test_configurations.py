
import os
import importlib
from src.utilities.validator import Validator


def test_configurations():
    configs = list(filter(
        lambda file: file.startswith("config_") and file.endswith(".py"),
        os.listdir("configs/")
    ))
    print(configs)
    for config in configs:
        print(f"IMPORTING {f'configs.{config[:-3]}'}")
        file = importlib.import_module(f"configs.{config[:-3]}")
        Validator.config(file.config)
