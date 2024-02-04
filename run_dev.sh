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

# Change directory to app
cd app

# Apply Django migrations
python manage.py migrate

# Start the Django development server
python manage.py runserver
