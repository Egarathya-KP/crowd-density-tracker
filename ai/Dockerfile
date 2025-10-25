
# Use official Python slim image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies for building packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install PyTorch first (CPU version, change for CUDA if needed)
RUN pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Install other Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install ByteTrack from GitHub
RUN pip install git+https://github.com/ifzhang/ByteTrack.git

# Copy the rest of the AI code
COPY . .

# Default command to run your inference script
CMD ["python", "inference_bytrack.py"]

