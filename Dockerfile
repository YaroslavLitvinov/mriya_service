# Use an official Python runtime as a base image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /mriya_service

# Copy the current directory contents into the container at /mriya_service
ADD . /mriya_service

# Install any needed packages specified in requirements.txt
RUN pip install -r mriya/requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME mriya_service
ENV PYTHONPATH $PYTHONPATH:/mriya_service/mriya/pybulk/sfbulk/:/mriya_service/mriya

# COPY startup script into known file location in container
COPY start.sh /start.sh
CMD ["/start.sh"]
