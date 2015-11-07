#! /usr/bin/python -B

import os.path
import datetime
import json

import wattmeter
import bme280

CONFIG_FILE = 'config.json'

if __name__ == '__main__':
    f = open(CONFIG_FILE, 'r')
    config = json.load(f)
    f.close()

    # date and datetime strings
    now = datetime.datetime.now()
    isodate = now.date().isoformat() # e.g. 2000-01-01
    isodatetime = now.isoformat()    # e.g. 2000-01-01T00:00:00.000000

    # output file
    logfile = config['logfile']
    is_firsttime = not os.path.exists(logfile)
    file = open(logfile, 'a')

    # create lock file
    lockfile = logfile + '.lock'
    lock = open(lockfile, 'w')
    lock.close()

    # wirte headers at the first time of each day
    if is_firsttime:
        file.write('datetime,' + bme280.csv_header() + ',' + wattmeter.csv_header() + '\n')

    # read measurements
    weather = bme280.read()
    watts   = wattmeter.read(config['serialport'], config['baudrate'])

    # write to log file
    file.write(isodatetime + ',')
    file.write(bme280.to_csv(weather) + ',')
    file.write(wattmeter.to_csv(watts) + '\n')
    file.close()

    # remove lock file
    os.remove(lockfile)
