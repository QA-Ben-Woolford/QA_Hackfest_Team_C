#!/bin/bash
echo "Update to latest dependcies"
sudo apt update && sudo apt upgrade -y 
echo "installing python"
sudo apt-get install python3.10 -y
echo "installing pip"
sudo apt install python3-pip -y
echo "installing requirements"
pip3 install -r requirements.txt 
echo "create database"
python3 create.py 
echo "run flask app"
gunicorn --bind=0.0.0.0:5000 app:app
#python3 app.py
EOF







