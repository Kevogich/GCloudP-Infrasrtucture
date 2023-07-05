# Use the official Python image as the base image
FROM python:3.9

# Copy the Python script to the container
COPY plant-simulation-script.py /app/plant-simulation-script.py

# Install any necessary dependencies 

RUN pip install google-cloud-pubsub


# Set the working directory
WORKDIR /app

# Run the Python script
CMD ["python", "plant-simulation-script.py"]
