#!/usr/bin/python
import os
import random
import time
import control

for x in range(1,10):
        os.system('docker start ubuntu'+ str(x))
i = 0 
while True:
        control = reload(control)
        print "Status: " + str(control.status)
        i+=1
        number = i
        if control.status == 1:
                _file = open('run.txt','a')
                _type = control.mType
                hours = control.mTime
                work = control.mWorker
                sl = control.numberIp
                print  'TYPE: ' + str(_type) + ' TIME: ' + str(hours) + ' SL: ' + str(sl) + ' WORKER: ' + str(work)
                _file.write(str(hours) + '\n')
                _file.write(str(sl) + '\n')
                for x in range(0,sl):
                        m = random.randint(1,9)
                        print 'RUN Ubuntu' +str(m)
                        tRun = 'docker exec -i -t -d ubuntu' + str(m) + ' bash -c ' + str("'") + "python /web/traffic.py --type " + str(_type) + " --hours " + str(hours) + " --worker " + str(work)  + " --number " + str(number) + " --delay " + str(random.choice(control.delay)) + " --file ubuntu" + str(m)
                        tFile = 'docker exec -i -t -d ubuntu' + str(m) + ' bash -c ' + str("'") + "python /web/traffic_file.py --type " + str(_type) + " --hours " + str(hours) + " --worker " + str(work)  + " --number " + str(number) + " --delay " + str(random.choice(control.delay))  + " --file ubuntu" + str(m)
                        _file.write(tFile + '\n')
                        os.system(tRun)
                _file.close()
                time.sleep(hours)
        time.sleep(2)
       

