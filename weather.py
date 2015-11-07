#! /usr/bin/python

import os.path
import datetime
import bme280

# date and datetime strings
now = datetime.datetime.now()
isodate = now.date().isoformat() # e.g. 2000-01-01
isodatetime = now.isoformat()    # e.g. 2000-01-01T00:00:00.000000

# output file
#logdir = '/ramdisk'
#logfile = logdir + '/weather-' + isodate + '.csv'

logfile = '/ramdisk/weather.csv'
is_firsttime = not os.path.exists(logfile)
file = open(logfile, 'a')

# create lock file
lockfile = logfile + '.lock'
lock = open(lockfile, 'w')
lock.close()

# wirte headers at the first time of each day
if is_firsttime:
    file.write('datetime,temperature,pressure,humidity\n')

# measure
measurements = bme280.readData()
#print measurements

# write to log file
file.write(isodatetime)
file.write(',{temperature:.2f},{pressure:.2f},{humidity:.2f}\n'.format(**measurements))
file.close()

# remove lock file
os.remove(lockfile)
