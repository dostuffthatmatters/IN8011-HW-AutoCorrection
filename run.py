
from src.main import Main
from configs.config_01 import config

if __name__ == "__main__":
    Main.run(config, timeout=15, line_numbers=True, execute=True)
