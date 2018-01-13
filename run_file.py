#!/usr/bin/python
import os
import time
import configFile
from pwn import *

_nameRun = configFile.fileRun+'.txt'
def connectSSH():
    if configFile.checkSSH == 0:
        s =  ssh(host=configFile.ipHack, user='root',password='Cnsc12345')
        if s.connected():
            sh = s.process('/bin/sh', env={'PS1':''})
            sh.sendline('/home/attacker/'+configFile.kichban+'/run;'+' exit')
            sh.recvall()
            s.close()
        else:
            connectSSH()
    if configFile.checkSSH == 1:
        time.sleep(float(20))
        s =  ssh(host=configFile.ipHack, user='attacker',password='Cnsc12345')
        if s.connected():
            sh = s.process('/bin/sh', env={'PS1':''})
            sh.sendline('echo 1 > /var/www/html/isAttack/'+configFile.kichban+"; exit")
            sh.recvall()
            s.close()
            time.sleep(float(90))
        else:
            connectSSH()
        
starttime =  time.time()
finishtime = starttime + float(configFile.timeRun)
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
        	if finishtime < time.time():
            		connectSSH()
        	time.sleep(float(_time))
for x in range(1,10):
        os.system('docker stop ubuntu'+ str(x))
        

