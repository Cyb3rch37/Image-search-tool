## Dockerfile (Containerized Deployment)
# Use the official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install build tools
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libdbus-1-dev \
    libdbus-glib-1-dev \
    cmake \
    && apt-get clean

# Install dependencies
RUN pip install pybind11

# Copy the requirements file
COPY requirements.txt /app/

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Copy the project files
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]