#!/bin/bash
sudo apt update && sudo apt upgrade -y 
sudo apt-get install python3.10 
sudo apt install python3-pip 
pip install -r requirements.txt 
python3 create.py 
python3 app.py
EOF


