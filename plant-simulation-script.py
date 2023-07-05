import time
import random
from google.cloud import pubsub_v1

# Set your Google Cloud project ID
project_id = "your-project-id"
topic_id = "sensor-data-topic"

# Create a PublisherClient
publisher = pubsub_v1.PublisherClient()

# Get the full topic path
topic_path = publisher.topic_path(project_id, topic_id)

def generate_sensor_data():
    # TODO-ADD MORE DATA
    return {
        "temperature": random.uniform(20, 30),
        "humidity": random.uniform(40, 60),
        "pressure": random.uniform(950, 1050),
    }

def publish_sensor_data(data):
    # Convert data to bytes
    data = str(data).encode("utf-8")

    # Publish the data to the Pub/Sub topic
    future = publisher.publish(topic_path, data=data)
    print(f"Published data: {data}")

if __name__ == "__main__":
    while True:
        # Generate random sensor data
        sensor_data = generate_sensor_data()

        # Publish the data to Pub/Sub
        publish_sensor_data(sensor_data)

        # Sleep for a few seconds (adjust as needed)
        time.sleep(1)
