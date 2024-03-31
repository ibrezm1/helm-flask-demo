# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set a build-time argument (public variable)
ARG PUBLIC_VARIABLE=default_public_value

# Set an environment variable during the build process
ENV PUBLIC_VARIABLE=${PUBLIC_VARIABLE}

# Set a secret environment variable during the run process
ENV SECRET_VARIABLE=default_secret_value

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable for Flask to run in production mode
ENV FLASK_ENV=production

# Expose port 5000 for Flask by default
EXPOSE 5000

# Define the command to run the app using Flask's built-in server
CMD ["flask", "run", "--host=0.0.0.0"]
