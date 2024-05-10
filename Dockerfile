FROM python:3.12

# Set a Linux-style working directory
WORKDIR /app

# Optional: labeling the author
LABEL authors="FMA"

# Copy the contents of the current directory on your host to /app in the container
ADD main.py .

# Install necessary Python packages
RUN pip install requests beautifulsoup4

# Expose port 4000 for your application
EXPOSE 4000

# Set an environment variable
ENV NAME World

# Command to run your Python application
CMD ["python", "main.py"]


