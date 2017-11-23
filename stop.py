#!/usr/bin/python
import os

for x in range(1,10):
        os.system('docker stop ubuntu'+ str(x))