import confluent_kafka as kafka
from settings.config import Config

POLL_TIMEOUT = 10  # Amount of time to poll of responses in seconds


class Producer:
    def __init__(self):
        kafka_servers = Config.KAFKA_CLUSTER_BOOTSTRAP_SERVERS
        api_key = Config.WRITER_API_KEY
        api_secret = Config.WRITER_API_SECRET
        self.servers = kafka_servers
        self.conf = {
            "bootstrap.servers": ",".join(self.servers),
            "compression.type": "snappy",
            "sasl.mechanism": "PLAIN",
            "security.protocol": "sasl_ssl",
            "sasl.username": api_key,
            "sasl.password": api_secret,
        }
        self.producer = kafka.Producer(self.conf)
        self.sent = 0

    def send(self, topic: str, key: str, value) -> None:
        print(f"sending data (key={key}, value={value}) to topic {topic}")

        def on_delivery(err, msg) -> None:
            """
            Reports the Failure or Success of a message delivery.
            Args:
                err : The Error that occurred while message producing.
                msg (Actual message): The message that was produced or failed.
            """
            if err and err.code() != kafka.KafkaError.NO_ERROR:
                print(f"Delivery failed {err.name()} - {err.str()} on message {msg.value()}")
            else:
                self.sent += 1
                print(f"message {self.sent}-{msg.key()} successfully produced to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")

        # Trigger any available delivery report callbacks from previous produce() calls
        self.producer.poll(0)

        try:
            # Asynchronously produce a message, the delivery report callback
            # will be triggered from poll() above, or flush() below, when the message has
            # been successfully delivered or failed permanently.
            self.producer.produce(topic=topic, key=key, value=value, on_delivery=on_delivery)

            # Wait for any outstanding messages to be delivered and delivery report
            # callbacks to be triggered.
            self.producer.flush()
        except BufferError:
            print(f"Buffer full ({len(self.producer)}), waiting for free space on the queue")
            self.producer.poll(POLL_TIMEOUT)
