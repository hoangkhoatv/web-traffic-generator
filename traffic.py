#!/usr/bin/python
# coding: utf-8
import sys, getopt
import re
import random
import time
import os
import threading
import config
import ftplib
import subprocess
import time
listIP = []
listAdd = []
def main(argv):
    ipfile = config.rootURLs
    addressfile = config.userAgent
    mType = ""
    numTime = ""
    numWorker = ""
    if os.path.exists("sqlmap") == False:
        os.system("git clone https://github.com/sqlmapproject/sqlmap.git")
    try:
        opts, args = getopt.getopt(argv,"hc:t:w",["type=","hours=","worker="])
    except getopt.GetoptError:
        print 'traffic.py -c typeTraffic -t timeGenerate '
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'tracffic.py -c <type> -t <time>'
            sys.exit()
        elif opt in ("-c", "--type"):
            mType = arg
        elif opt in ("-t", "--hours"):
            numTime = arg
        elif opt in ("-w", "--worker"):
            numWorker = arg
    print "Type: "+ str(mType) + "Time: " + str(numTime) + "Worker: " + str(numWorker)
    start_time = time.time()
    end_time = start_time + float(numTime)
    while True:
        now_time = time.time()
        if mType == '0':
            t = threading.Thread(target=workerNormal)
            t.start()
        elif mType == '1':
            trafficGenerator(0,5)
        elif mType == '2':
            trafficGenerator(int(numWorker),int(numWorker)
        if now_time > end_time:
            print "Finish"
            break
def trafficGenerator(ranType1,ranType2):
    ran = random.randint(ranType1,ranType2)
    print ran
    if ran == 0:
        t = threading.Thread(target=workerNmap)
    elif ran == 1:
        t = threading.Thread(target=workerPing)
    elif ran == 2:
        t = threading.Thread(target=workerFTP)
    elif ran == 3:
        t = threading.Thread(target=workerSqlmap)
    elif ran == 4:
        t = threading.Thread(target=workerDns)
    else:
        t = threading.Thread(target=workerWeb)
        t1 = threading.Thread(target=workerNormal)
        t1.start()
    t.start()

def workerNmap():
    ip = random.choice(config.ipList)
    ran = random.randint(0,6)
    if ran == 0:
        os.system("nmap " + ip)
    elif ran == 1:
        os.system("nmap –vv –n –sS " + ip)
    elif ran == 2:
        os.system("nmap –vv –n –sT " + ip)
    elif ran == 3:
        os.system("nmap –vv –n –sF " + ip)
    elif ran == 4:
        os.system("nmap –vv –n –sU " + ip)
    elif ran == 5:
        os.system("nmap –vv –sA " + ip)
    else:
        os.system("nmap –vv –sP " + ip)
def workerPing():
    ran = random.randint(1,20)
    response = os.system("ping -c " + str(ran) + " " + random.choice(config.ipList))
def workerNormal():
    os.system("curl -A '" +   random.choice(config.userAgent) + "' -O" + random.choice(config.urlDKHC) )
    os.system("curl -A '" +   random.choice(config.userAgent) + "' -O" + random.choice(config.urlOneShop) )
    os.system("curl -A '" +   random.choice(config.userAgent) + "' -O" + random.choice(config.urlNoiThat) )
def workerFTP():
    server = ftplib.FTP()
    server.connect(random.choice(config.ipList))
    ran = random.randint(1,20)
    for x in range(0, ran):
        server.login('cnsc','123456')
def workerWeb():
    rPacket = random.randint(0,100)
    os.system('python dos.py 000000000 ' + str(rPacket))
def workerSqlmap():
    p = subprocess.Popen("python /web/sqlmap/sqlmap.py -u "+ random.choice(config.urlWeb) +"  --risk=3 --level=5 --batch", shell=True)
    ran = random.randint(5,20)
    time.sleep(ran)
    p.kill()
def workerDns():
    os.system("nslookup -type=any " + random.choice(config.urlDNS))
    os.system("nslookup -type=any " + random.choice(config.ipDNS))
# def extractIPs(fileContent):
#     pattern = r"((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)([ (\[]?(\.|dot)[ )\]]?(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3})"
#     ips = [each[0] for each in re.findall(pattern, fileContent)]   
#     for item in ips:
#         location = ips.index(item)
#         ip = re.sub("[ ()\[\]]", "", item)
#         ip = re.sub("dot", ".", ip)
#         ips.remove(item)
#         ips.insert(location, ip) 
#     return ips

# def readFile(urlIp,urlAddress):
#     file1 = open(urlIp,"r")
#     for line in file1:
#         listIP.append(line.strip())
    
#     file2 = open(urlAddress,"r")
#     for line in file2:
#         listAdd.append(line.strip())
if __name__ == "__main__":
   main(sys.argv[1:])
