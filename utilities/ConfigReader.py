import os
from configparser import ConfigParser


def read_config(section, key):
    config = ConfigParser()
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Directory where ConfigReader.py is located
    config_path = os.path.join(base_dir, "..", "Config", "conf.ini")  # Navigate to conf.ini

    config.read(config_path)
    return config.get(section, key)
