#!/bin/bash

sudo apt update
sudo apt install python3
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m pytest --cov
