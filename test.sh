#!/bin/bash

sudo apt-get update
sudo apt install chromium-browser -y
sudo apt install wget unzip -y
version=$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$(chromium-browser --version | grep -oP 'Chromium \K\d+'))
wget https://chromedriver.storage.googleapis.com/${version}/chromedriver_linux64.zip
sudo unzip chromedriver_linux64.zip -d /usr/bin
rm chromedriver_linux64.zip
sudo apt-get install python3-pip python3-venv -y
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m pytest --cov=application --cov-report html

export db_uri
export secretkey

python3 create.py
gunicorn --workers=4 --bind=0.0.0.0:5000 app:app
