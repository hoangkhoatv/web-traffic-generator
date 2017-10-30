#!/usr/bin/python

import sys, getopt
import re
import random
import time
import os
import threading
import config

listIP = []
listAdd = []
def main(argv):
    ipfile = config.rootURLs
    addressfile = config.userAgent
    print 'IP file is "', ipfile
    print 'Address file is "', addressfile
    try:
        opts, args = getopt.getopt(argv,"hi:a:",["ifile=","afile="])
    except getopt.GetoptError:
        print 'traffic.py -i <ipfile> -a <addressfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'tracffic.py -i <ipfile> -oa<addressile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            ipfile = arg
        elif opt in ("-a", "--afile"):
            addressfile = arg
        
    print 'IP file is "', ipfile
    print 'Address file is "', addressfile
   readFile(ipfile,addressfile)
   while True:
       rIP = random.randint(0,len(listIP)-1)
       rAdd = random.randint(0,len(listAdd)-1)
       rTime = random.uniform(0.1,2)
       t = threading.Thread(target=worker,args=(listIP[rIP],listAdd[rAdd]))
       t.start()
       print rTime
       time.sleep(rTime)

def worker(ip,add,num):
    os.system('curl --interface '+ ip + ' ' + add)
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

def readFile(urlIp,urlAddress):
    file1 = open(urlIp,"r")
    for line in file1:
        listIP.append(line.strip())
    
    file2 = open(urlAddress,"r")
    for line in file2:
        listAdd.append(line.strip())
if __name__ == "__main__":
   main(sys.argv[1:])
