import os
import json
from datetime import datetime
from settings.config import Config
from drink_data_publisher import LCBODrinkPublisher

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
                        publisher.produce(json_content)
                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON in {file_name}: {e}")

    except OSError as e:
        print(f"Error reading files in {path}: {e}")


RUN_DATE = Config.RUN_DATE
if not RUN_DATE:
    date = str(datetime.now().date())
    print(f"date: {date}")
    print(f"Run date is not passed. The default date is {date}")
    RUN_DATE = date
publisher = LCBODrinkPublisher()
FILE_PATH = FILE_PATH + "/" + RUN_DATE
read_files(FILE_PATH)
