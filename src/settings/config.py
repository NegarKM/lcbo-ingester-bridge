import os
from typing import Final


class Config(object):
    LCBO_FILES_PATH: Final = os.environ.get("LCBO_FILES_PATH")
