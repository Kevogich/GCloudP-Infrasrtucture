#Uses Modbud to communicate between devices 
#Uses Pub/Sub to subscribe to messages . Ingest and distribute

from pymodbus.client.sync import ModbusSerialClient
from google.cloud import pubsub

# Modbus Configuration
modbus_port = '/dev/ttyUSB0'  # Replace with device port (or api???)
modbus_baudrate = 9600  # device baudrate

# Pub/Sub Configuration
project_id = 'project-id'  # CP project ID
topic_name = 'sensor-data-topic'  # Pub/Sub topic name

# Connect to Modbus device
client = ModbusSerialClient(method='rtu', port=modbus_port, baudrate=modbus_baudrate)
client.connect()

# Connect to Pub/Sub
publisher = pubsub.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)

# Read sensor data from Modbus device and publish to Pub/Sub
def read_and_publish_sensor_data():
    # Read sensor values from Modbus registers
    register_address = 0  # Replace with the Modbus register address to read from
    register_count = 4  # Replace with the number of registers to read
    response = client.read_holding_registers(register_address, register_count)

    if response.isError():
        print(f"Error reading Modbus registers: {response}") #log this error for reporting ??
    else:
        sensor_data = response.registers  # Get the sensor data from the response
        print(f"Sensor Data: {sensor_data}")

        # Publish sensor data to Pub/Sub topic
        message_data = ','.join(str(val) for val in sensor_data).encode('utf-8')
        publisher.publish(topic_path, data=message_data)
        print("Sensor data published to Pub/Sub")

# Call the function to continuously read and publish sensor data (OPTIMIZE WITH CRON IF acceptable downtime intervals)
while True:
    read_and_publish_sensor_data()
