FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt ./

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt


# Copy the application files
COPY . .

# Specify the default command
CMD ["python", "app.py"]
