
# Use an official Python runtime as a parent image
FROM python:2.7-slim
RUN apt-get update && apt-get install -y supervisor

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified
RUN pip install requests

# Run app.py when the container launches
CMD ["/usr/bin/supervisord", "-c", "./stress-manager.conf"]