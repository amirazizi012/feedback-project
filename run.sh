#!/bin/bash
echo "Starting Feedback Board Setup..."

# Check if python3 is installed
if ! command -v python3 &> /dev/null
then
    echo "Error: python3 could not be found"
    exit
fi

# Create venv if not exists
if [ ! -d "venv" ]; then
    echo "Creating Virtual Environment..."
    python3 -m venv venv
fi

# Activate venv
source venv/bin/activate

# Install requirements
echo "Installing Requirements..."
pip install -r requirements.txt

# Start server
echo "Starting Server at http://127.0.0.1:8000"
uvicorn app.main:app --reload
