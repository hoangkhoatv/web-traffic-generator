#!/usr/bin/python
import os
import random
import time
import control

for x in range(1,10):
        os.system('docker start ubuntu'+ str(x))
while True:
        _type = control.mType
        hours = control.mTime
        work = control.mWorker
        sl = random.randint(1,9)
        print  'TYPE: ' + str(_type) + ' TIME: ' + str(hours) + ' SL: ' + str(sl) + ' WORKER: ' + str(work)
        for x in range(0,sl):
                m = random.randint(1,9)
                print 'RUN Ubuntu' +str(m)
                os.system('docker exec -i -t -d ubuntu' + str(m) + ' bash -c ' + str("'") + "python /web/traffic.py --type " + str(type) + " --hours " + str(hours) + " --worker " + str(work)  + str("'"))
        time.sleep(hours)

