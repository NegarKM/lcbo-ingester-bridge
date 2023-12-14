import os
import json
from settings.config import Config

FILE_PATH = Config.LCBO_FILES_PATH


def read_files(path):
    try:
        files = os.listdir(path)

        for file_name in files:
            file_path = os.path.join(path, file_name)

            if os.path.isfile(file_path):
                with open(file_path, 'r') as file:
                    try:
                        json_content = json.load(file)

                        print(f"Attributes and values in {file_name}:")
                        for key, value in json_content.items():
                            print(f"{key}: {value}")

                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON in {file_name}: {e}")

    except OSError as e:
        print(f"Error reading files in {path}: {e}")


read_files(FILE_PATH)
