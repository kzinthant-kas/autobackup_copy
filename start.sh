#!/bin/bash

curl https://rclone.org/install.sh | tac | tac| sudo bash

python3 schedule.py

