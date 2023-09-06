FROM python:3.9-slim-buster

LABEL version="1.0" \
    name="waterbalance-flask-rest-api"

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    libgdal-dev \
    && apt-get clean

# Set environment variables for GeoPandas
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

# Install pip and upgrade it
RUN python -m pip install --upgrade pip

COPY . /app

# Set the working directory
WORKDIR /app

# Copy the Python requirements file into the container
COPY requirements.txt .

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# # Copy the rest of your application code into the container
# COPY . .

# Specify the command to run your application
CMD ["python3", "app.py"]
