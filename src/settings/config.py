import os
from typing import Final


class Config(object):
    LCBO_FILES_PATH: Final = os.environ.get("LCBO_FILES_PATH")
    RUN_DATE = os.environ.get("RUN_DATE")
    KAFKA_CLUSTER_BOOTSTRAP_SERVERS = os.environ.get("KAFKA_CLUSTER_BOOTSTRAP_SERVERS")
