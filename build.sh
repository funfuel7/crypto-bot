#!/bin/bash
# Set up isolated Python environment
python -m venv venv
source venv/bin/activate

# Force upgrade core packages
python -m pip install --upgrade --force-reinstall pip setuptools wheel

# Install requirements with no cache
pip install --no-cache-dir -r requirements.txt
