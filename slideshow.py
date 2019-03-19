#!/usr/bin/env python3

flash_drive = "FA26-2330"

import subprocess
from time import sleep

# Read from flash drive
path = "/media/pi/" + flash_drive

while True:
    files = subprocess.run(['ls', path], stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n')
    if len(files) > 1:
        break
    sleep(1)

cmd = 'feh -Y -x -q -D 4 -B black -F -Z -r /media/pi/' + flash_drive + '/'
subprocess.run(cmd.split(' '), stdout=subprocess.PIPE)
