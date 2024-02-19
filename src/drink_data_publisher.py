import time
import json

from producer import Producer

topic = "lcbo-test-events"
# topic = "lcbo-drinks-data"


class LCBODrinkPublisher:
    def __init__(self):
        self.producer = Producer()

    def produce(self, data: dict) -> None:
        self.producer.send(topic=topic, key=f"lcbo_drink_{time.time()}", value=json.dumps(data))
