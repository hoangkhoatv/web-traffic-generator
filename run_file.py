#!/usr/bin/python
import os
import time
import configFile
_nameRun = "/web/"+configFile.fileRun+'.txt'
i = 0
_fileRun = open(_nameRun,'r')
while True:
    _time = _fileRun.readline()
    if _time == '':
         _fileRun.close
         break
    _number = _fileRun.readline()
    ran = int(_number.strip())
    for x in range(0,ran):
        print _fileRun.readline()
        os.system(_fileRun.readline())
    time.sleep(_time)

