#! /usr/bin/python

import serial
import json
import time

def csv_header():
    return 'volt,ampere,watt,volt-ampere,power-factor'

def to_csv(dict):
    return '{V:.2f},{A:.2f},{W:.2f},{VA:.2f},{PF:.2f}'.format(**dict)

def read(port, baudrate):
    com = serial.Serial(port, baudrate)
    com.flush()

    dict = []
    csvline = ''
    while csvline == '':
        try:
            dict = json.loads(com.readline())
            csvline = to_csv(dict)
        except ValueError:
            pass
        except KeyError:
            pass

    com.close()
    return dict

if __name__ == '__main__':
    print csv_header()
    print to_csv(read('/dev/ttyACM0', 115200))
