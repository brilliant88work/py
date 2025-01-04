# Base Image
FROM python:3.12.8-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . /app/

# Expose port 8000 for the Django development server
EXPOSE 8000

# Run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

