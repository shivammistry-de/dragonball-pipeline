# 1. Use an official Python runtime as a parent image
# This provides a lightweight environment with Python 3.9 pre-installed.
FROM python:3.9-slim

# 2. Set the working directory inside the container
# All subsequent commands (like COPY, RUN, CMD) will be executed from this path.
WORKDIR /app

# 3. Copy the dependency file and install dependencies
# We copy only this file first to take advantage of Docker's layer caching.
# If requirements.txt doesn't change, Docker will reuse this layer on future builds.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the application code into the container
# This copies our main script into the /app directory inside the container.
COPY app.py .

# 5. Define the command to run when the container starts
# This tells Docker to execute "python app.py" when the container is run.
CMD ["python", "app.py"]
