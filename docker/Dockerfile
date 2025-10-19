# Base image with python
FROM python:3.12-slim

# Set the working directory to /app
WORKDIR /app

# Copy the dependencies file 
COPY all_packages.txt /app/

# Install the project dependencies
RUN pip install --no-cache-dir -r all_packages.txt

# Copy the project files
COPY . /app

# Expose port 5000 for the Flask app
EXPOSE 5000

# Comand default to run the app
CMD ["python", "app.py"]