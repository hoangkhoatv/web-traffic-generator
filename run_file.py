#!/usr/bin/python
import os
import time
import configFile
_nameRun = configFile.fileRun+'.txt'
for x in range(1,10):
        os.system('docker start ubuntu'+ str(x))
with open(_nameRun,'r') as _fileRun:
	while True:

    		_time = _fileRun.readline()
		print "TIME: " + _time
    		if _time == '': 
         		break
    		_number = _fileRun.readline()
    		ran = int(_number.strip())
		print "IP: " + _number
    		for x in range(0,ran+1):
        		print _fileRun.readline()
       			os.system(_fileRun.readline())
    		time.sleep(float(_time))

