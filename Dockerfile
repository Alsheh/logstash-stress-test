# Use an official Python runtime as a parent image
FROM python:2.7-slim
RUN apt-get update && apt-get install -y supervisor

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified
RUN pip install requests

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
#CMD ["python", "get_reqeust.py", "http://localhost"]%
CMD ["/usr/bin/supervisord", "-c", "./stress-manager.conf"]