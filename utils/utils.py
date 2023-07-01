import os
from box.exceptions import BoxValueError
import yaml 
from ensure import ensure_annotations
from box import ConfigBox
from src.logging import logger
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read the yaml file and return a ConfigBox instance
       Args: 
            path_to_yaml(str): Path to the yaml file
       Raises: 
            FileNotFound: if no file is found
            YAMLError: if the yaml file is not correctly formatted
        Returns:

    """
    try:
        with open(path_to_yaml, 'r') as f:
                config = yaml.safe_load(f)
                logger.info(f"Yaml file: %s loaded successfully." % path_to_yaml)
                return ConfigBox(config)
    except FileNotFoundError:
            raise BoxValueError(f"{path_to_yaml} not found")
    except yaml.YAMLError as e:
            raise BoxValueError(f"{path_to_yaml} is not a valid yaml file") from e

@ensure_annotations
def create_directory(path_to_directory: list, verbose=True):
      """Create a directory

        Args:
            path_to_directory (list): path to directory
            ignore_log (bool): whether to ignore multiple directories creation. Defaults to False      
        """
      for path in path_to_directory:
            os.makedirs(path, exist_ok=True)
            if verbose:
                  logger.info(f"Created directory: {path}")

@ensure_annotations
def get_file_size(path: Path) -> str:
    """ Get the size of the file

        Args:
            path (Path): Path to the file
        Returns:
            str: Size of the file in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f" ~ {size_in_kb} KB"
