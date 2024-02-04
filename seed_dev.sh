#!/bin/bash

# Check if the venv directory exists
if [ ! -d "venv" ]; then
    # Create a virtual environment if it doesn't exist
    python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Install required packages
pip install -r requirements.txt

# Install pre-commit and faker explicitly
pip install pre-commit faker

# Change directory to app
cd app

# Apply Django migrations
python manage.py migrate

python manage.py create_employees 100
python manage.py create_sbi 100