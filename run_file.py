#!/usr/bin/python
import os
import time
import configFile
from pwn import *

_nameRun = configFile.fileRun+'.txt'
def connectSSH():
    if configFile.checkSSH:
        s =  ssh(host=configFile.ipHack, user='root',password='Cnsc12345')
        if s.connected():
            sh = s.process('/bin/sh', env={'PS1':''})
            sh.sendline('/home/attacker/'+configFile.kichban+'/run;'+' exit')
            sh.recvall()
            s.close()
        else:
            connectSSH()
    else:
        time.sleep(float(60))
        s =  ssh(host=configFile.ipHack, user='root',password='Cnsc12345')
        if s.connected():
            sh = s.process('/bin/sh', env={'PS1':''})
            sh.sendline('echo 1 > /var/www/html/isActtack/'+configFile.kichban+"; exit")
            sh.recvall()
            s.close()
            time.sleep(float(180))
        else:
            connectSSH()
        
starttime =  time.time()
finishtime = starttime + configFile.timeRun
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
        if(finishtime > time.time()){
            connectSSH()
        }
        time.sleep(float(_time))
        

