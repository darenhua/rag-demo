# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Install gcc and python3-dev
RUN apt-get update && apt-get install gcc python3-dev

COPY requirements.txt .

# Install jupyter and python packages
RUN pip install -r requirements.txt

# Set the working directory in the container
WORKDIR /src

# Copy the current directory contents into the container at /app
COPY ./src /src

# Make port 80 available to the world outside this container
EXPOSE 8080

# Define environment variable
# ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
