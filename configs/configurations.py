"""PaperGPT configurations parser module."""

import yaml
from typing import Dict

def init( ) -> None:
    global config

    # open and parse configurations   
    with open("configs/configurations.yaml", "r") as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)