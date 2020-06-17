#!/bin/bash

# Create a folder for the app
mkdir ~/PiHub
cd ~/PiHub

# Get the IoT central connection details
echo What is the Azure IoT Central ID Scope?
read id_scope

echo What is the Azure IoT Central Primary or Secondary Key?
read key

# Create the .env file
echo "ID_SCOPE=$id_scope" >> ~/PiHub/.env
echo "IOT_CENTRAL_KEY=$key" >> ~/PiHub/.env

# Download the app files
echo Downloading files...

curl -L -o ~/PiHub/requirements.txt https://github.com/jimbobbennett/smart-garden-ornaments/releases/download/v1.0/requirements.txt
curl -L -o ~/PiHub/app.py https://github.com/jimbobbennett/smart-garden-ornaments/releases/download/v1.0/app.py
curl -L -o ~/PiHub/mappings.py https://github.com/jimbobbennett/smart-garden-ornaments/releases/download/v1.0/mappings.py

# Install the Python requirements
echo Installing requirements...

python3 -m venv .venv

source ./.venv/bin/activate

pip3 install -r ~/PiHub/requirements.txt
