#!/usr/bin/python
# coding: utf-8
import sys, getopt
import re
import random
import time
import os
import threading
import config
import subprocess
import time


def main(argv):
    ipfile = config.rootURLs
    addressfile = config.userAgent
    mType = ""
    numTime = ""
    numWorker = ""
    number = 0
    delay = 0
    list = []
    # if os.path.exists("sqlmap") == False:
    #     os.system("git clone https://github.com/sqlmapproject/sqlmap.git")
    try:
        opts, args = getopt.getopt(argv,"hc:t:w:n:d",["type=","hours=","worker=","number=","delay="])
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
    if mType == '0':
        t = threading.Thread(target=workerNormal, args = (10,number,))
        t.start()
    elif mType == '1':
        t = threading.Thread(target=workerNormal, args = (9,number,))
        t.start()
        trafficGenerator(0,6,1,number)
    elif mType == '2':
        t = threading.Thread(target=workerNormal, args = (8,number,))
        t.start()
        trafficGenerator(0,6,2,number)
    elif mType == '3':
        t = threading.Thread(target=workerNormal, args = (7,number,))
        t.start()
        trafficGenerator(0,6,3,number)
    elif mType == '4':
        t = threading.Thread(target=workerNormal, args = (6,number,))
        t.start()
        trafficGenerator(0,6,4,number)
    elif mType == '5':
        t = threading.Thread(target=workerNormal, args = (5,number,))
        t.start()
        trafficGenerator(0,6,5,number)
    elif mType == '6':
        trafficGenerator(int(numWorker),int(numWorker),10,number)
    
def trafficGenerator(ranType1,ranType2,num,number):
    for x in range(1,num):
        ran = random.randint(ranType1,ranType2)
        if ran == 0:
            t = threading.Thread(target=workerNmap, args = (number,))
        elif ran == 1:
            t = threading.Thread(target=workerPing, args = (number,))
        elif ran == 2:
            t = threading.Thread(target=workerFTP, args = (number,))
        elif ran == 3:
            t = threading.Thread(target=workerSqlmap, args = (number,))
        elif ran == 4:
            t = threading.Thread(target=workerDns, args = (number,))
        elif ran == 5:
            t = threading.Thread(target=workerWebDos, args = (number,))
        t.start()

def workerNmap(number):
    ip = random.choice(config.ipList)
    ran = random.randint(0,6)
    for x in range(random.ranint(10,20)):
        if ran == 0:
            strRun = "nmap " + ip
        elif ran == 1:
            strRun = "nmap –vv –n –sS " + ip
        elif ran == 2:
            strRun = "nmap –vv –n –sT " + ip
        elif ran == 3:
            strRun = "nmap –vv –n –sF " + ip
        elif ran == 4:
            strRun = "nmap –vv –n –sU " + ip
        elif ran == 5:
            strRun = "nmap –vv –sA " + ip
        else:
            strRun = "nmap –vv –sP " + ip
        _file = open('traffic'+str(number)+'.txt','a')
        _file.write(strRun + '\n')
        _file.close()
        os.system(strRun)
        time.sleep(delay)
def workerPing(number):
    ran = random.randint(10,20)
    response = "ping -c " + str(ran) + " " + random.choice(config.ipList)
    _file = open('traffic'+str(number)+'.txt','a')
    _file.write(response + '\n')
    _file.close()
    os.system(response)
def workerNormal(num,number):
    for x in range(1,5):
        p1 = 'curl -A "' +   random.choice(config.userAgent) + '" ' + random.choice(config.urlDKHC)
        p2 = 'curl -A "' +   random.choice(config.userAgent) + '" ' + random.choice(config.urlOneShop)
        p3 = 'curl -A "' +   random.choice(config.userAgent) + '" ' + random.choice(config.urlNoiThat)
        _file = open('traffic'+str(number)+'.txt','a')
        _file.write(p1 + '\n')
        _file.write(p2 + '\n')
        _file.write(p3+ '\n')
        _file.close()
        subprocess.Popen(p1, shell=True)
        subprocess.Popen(p2, shell=True)
        subprocess.Popen(p3, shell=True)
        t = threading.Thread(target=workerWeb)
        t.start()
        time.sleep(delay)

def workerFTP(number):
    strRun = 'curl ftp://'+ random.choice(config.ipList) + ' --user cnsc:123456'
    ran = random.randint(10,20)
    for x in range(0, ran):
        _file = open('traffic'+str(number)+'.txt','a')
        _file.write(strRun + '\n')
        _file.close()
        os.system(strRun)
        time.sleep(delay)
    
        
def workerWeb(number):  
    cmnd = random.randint(100000000,999999999)
    strRun = 'python /web/dos.py ' + str(cmnd) + ' ' + str(cmnd)
    _file = open('traffic'+str(number)+'.txt','a')
    _file.write(strRun + '\n')
    _file.close()
    os.system(strRun)

def workerWebDos(number):  
    cmnd = random.randint(100000000,999999999)
    for x in range(0,random.randint(10,20)):
        strRun = 'python /web/dos.py ' + str(cmnd) + ' ' + str(cmnd + x)
        _file = open('traffic'+str(number)+'.txt','a')
        _file.write(strRun + '\n')
        _file.close()
        os.system(strRun)
        time.sleep(delay)
def workerSqlmap(number):
    _file = open('traffic'+str(number)+'.txt','a')
    strRun = "python /web/sqlmap/sqlmap.py -u '"+ random.choice(config.urlDKHC) +"'  --risk=3 --level=5 --batch"
    _file.write(strRun + '\n')
    _file.close()
    p = subprocess.Popen(strRun, shell=True)
    time.sleep(10)
    p.kill()
def workerDns(number):
    for x in range(random.randint(5,10)):
        n1 = "nslookup -type=any " + random.choice(config.urlDNS)
        n2 = "nslookup -type=any " + random.choice(config.ipDNS)
        _file = open('traffic'+str(number)+'.txt','a')
        _file.write(n1 + '\n')
        _file.write(n2 + '\n')
        _file.close()    
        os.system(n1)
        os.system(n2)
        time.sleep(delay)

if __name__ == "__main__":
   main(sys.argv[1:])
