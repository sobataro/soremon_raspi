#! /usr/bin/python

import serial
import json
import time

def csv_header():
    return 'volt,ampere,watt,volt-ampere,power-factor'

def read_watts():
    com = serial.Serial(
        port='/dev/ttyACM0',
        baudrate=115200
    )

    com.flush()

    csvline = ''
    while csvline == '':
        try:
            line = json.loads(com.readline())
            csvline = '{V:.2f},{A:.2f},{W:.2f},{VA:.2f},{PF:.2f}'.format(**line)
        except ValueError:
            pass
        except KeyError:
            pass

    com.close()
    return csvline

if __name__ == '__main__':
    print csv_header()
    print read_watts()
