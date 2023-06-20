import random
import time
from datetime import datetime
from google.api_core import exceptions
from google.cloud import pubsub

# GCP project configuration
project_id = "myproject-id"
topic_name = "humidifier-sensor-data"

# Humidity range (in percentage)
min_humidity = 40
max_humidity = 70

# Number of sensors
num_sensors = 5

# Initialize the Pub/Sub publisher client
publisher = pubsub.PublisherClient()

# Generate random humidity values for each sensor and publish to Pub/Sub topic
while True:
    for sensor_id in range(1, num_sensors + 1):
        try:
            # Generate random humidity value
            humidity = random.uniform(min_humidity, max_humidity)

            # Get current timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Create the message payload
            data = {
                "sensor_id": sensor_id,
                "humidity": humidity,
                "timestamp": timestamp
            }

            # Publish the message to the Pub/Sub topic
            publisher.publish(f"projects/{project_id}/topics/{topic_name}", str(data).encode())

            print(f"Published data: Sensor ID = {sensor_id}, Humidity = {humidity}%, Timestamp = {timestamp}")
            
        #TO-DO -Intergrate with given error codes 
        except exceptions.GoogleAPICallError as e:
            # Error occurred while publishing data
            print(f"Error publishing data for Sensor ID {sensor_id}: {e.code()}")
            # Add error handling logic here
            # ...

        except Exception as e:
            # Other unexpected errors occurred
            print(f"Error occurred for Sensor ID {sensor_id}: {str(e)}")
            # Add error handling logic here
            # ...

    # Delay for 1 second before publishing the next set of messages
    time.sleep(1)
