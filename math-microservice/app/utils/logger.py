import logging
from kafka import KafkaProducer
import json

# Create a logger
logger = logging.getLogger("math_microservice_logger")
logger.setLevel(logging.INFO)

# === File Handler ===
file_handler = logging.FileHandler("logs.txt")
file_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add handler to logger (avoid duplication)
if not logger.handlers:
    logger.addHandler(file_handler)

# === Kafka Producer ===
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def log_to_kafka(topic: str, message: dict):
    producer.send(topic, message)
    producer.flush()
    # Also log to file
    logger.info(f"Logged to Kafka on topic '{topic}': {message}")
