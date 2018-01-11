
#!/usr/bin/python
# coding: utf-8
import sys, getopt
import re
import random
import time
import os
import threading
import configFile
import subprocess
import time
def main(argv):
    _nameFolder = "/web/"+configFile.fileTraffic + "/"
    mType = ""
    numTime = ""
    numWorker = ""
    number = 0
    delay = 0
    try:
        opts, args = getopt.getopt(argv,"hc:t:w:n:d:f",["type=","hours=","worker=","number=","delay=","file="])
    except getopt.GetoptError:
        print 'traffic.py -c typeTraffic -t timeGenerate '
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'traffic.py -c <type> -t <time>'
            sys.exit()
        elif opt in ("-c", "--type"):
            mType = arg
        elif opt in ("-t", "--hours"):
            numTime = arg
        elif opt in ("-w", "--worker"):
            numWorker = arg
        elif opt in ("-n", "--number"):
            number = arg
        elif opt in ("-d", "--delay"):
            delay = arg
        elif opt in ("-f", "--file"):
            nameFile = arg
    _fileRun = open(_nameFolder+nameFile+number+".txt",'r')
    
    while True:
        _cmd = _fileRun.readline()
        os.system(_cmd)
        _time = _fileRun.readline()
        if _time == '':
            _fileRun.close
            break
        time.sleep(_time)

if __name__ == "__main__":
   main(sys.argv[1:])