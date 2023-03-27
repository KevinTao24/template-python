# Use an official Python runtime as a parent image
FROM python:3.11.2

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Poetry
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# # Install any needed packages specified in poetry.lock
# RUN poetry install

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME Tao

# Run main.py when the container launches
CMD ["python", "src/__main__.py"]