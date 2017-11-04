#!/usr/bin/python
import sys, getopt
import re
import random
import time
import os
import threading
import config
import ftplib
import subprocess
listIP = []
listAdd = []
def main():
    ipfile = config.rootURLs
    addressfile = config.userAgent
    print 'IP file is "', ipfile
    print 'Address file is "', addressfile
#     try:
#         opts, args = getopt.getopt(argv,"hi:a:",["ifile=","afile="])
#     except getopt.GetoptError:
#         print 'traffic.py -i <ipfile> -a <addressfile>'
#         sys.exit(2)
#     for opt, arg in opts:
#         if opt == '-h':
#             print 'tracffic.py -i <ipfile> -oa<addressile>'
#             sys.exit()
#         elif opt in ("-i", "--ifile"):
#             ipfile = arg
#         elif opt in ("-a", "--afile"):
#             addressfile = arg
        
#     print 'IP file is "', ipfile
#     print 'Address file is "', addressfile
#    readFile(ipfile,addressfile)
    while True:
        rTime = random.randint(20,40)
        ran = random.randint(0,4)
        if ran == 0:
           t = threading.Thread(target=workerNmap)
        elif ran == 1:
            t = threading.Thread(target=workerPing)
        elif ran == 2:
            t = threading.Thread(target=workerFTP)
        elif ran == 3:
            t = threading.Thread(target=workerSqlmap)
        else:
            t = threading.Thread(target=workerWeb)
        t.start()
        print rTime
        time.sleep(rTime)
        t.close()

# def worker(ip,add,num):
#     os.system('curl --interface '+ ip + ' ' + add)
def workerNmap():
    ip = random.choice(config.ipList)
    ran = random.randint(0,6)
    if ran == 0:
        os.system('nmap ' + ip)
    elif ran == 1:
        os.system('nmap –vv –n –sS ' + ip)
    elif ran == 2:
        os.system('nmap –vv –n –sT ' + ip)
    elif ran == 3:
        os.system('nmap –vv –n –sF ' + ip)
    elif ran == 4:
        os.system('nmap –vv –n –sU ' + ip)
    elif ran == 5:
        os.system('nmap –vv –sA ' + ip)
    else:
        os.system('nmap –vv –sP ' + ip)
def workerPing():
    ran = random.randint(0,20)
    response = os.system("ping -c " + ran + " " + random.choice(config.ipList))
def workerFTP();
    server = ftplib.FTP()
    server.connect(random.choice(config.ipList))
    ran = random.randint(1,20)
    for x in range(0, ran):
        server.login('cnsc','123456')
def workerWeb():
    rPacket = random.randint(0,100)
    os.system('python dos.py 000000000 ' + str(rPacket))
def workerSqlmap():
    p = subprocess.Popen("python sqlmap/sqlmap.py -u "+ random.choice(config.urlWeb) +"  --risk=3 --level=5 --batch", shell=True)
    ran = random.randint(5,30)
    time.sleep(ran)
    p.kill()

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
   main()
