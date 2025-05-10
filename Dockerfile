FROM python:3.9-slim

WORKDIR /app

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code to /app/app
COPY ./app /app/app

# Switch to the app directory
WORKDIR /app/app
# CMD ["/bin/sh", "-c", "cd app && uvicorn main:app --host 0.0.0.0 --port 8000"]

# Run uvicorn directly
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]