import random
import time
import os
import threading

def main():
    while True:
        rPacket = random.randint(0,100)
        rTime = random.randint(0,4)
        #for x in range(0, rPacket):
        os.system('python dos.py 000000000 ' + str(rPacket))
        time.sleep(rTime)

if __name__ == "__main__":
   main()