# syntax=docker/dockerfile:1
FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Install uv (modern Python dependency manager)
RUN pip install --upgrade pip && pip install uv

# Copy project files
COPY . .

# Install dependencies with uv
RUN uv sync

# Expose port (optional, for API servers)
EXPOSE 8000

# Default command (can be overridden)
CMD ["python", "main.py"]
