#!/bin/bash

sudo apt-get update
sudo apt-get install python3
sudo apt-get install python3-venv
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m pytest --cov
