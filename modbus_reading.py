#!/usr/bin/env python
# 
import minimalmodbus
import numpy as np
import matplotlib.pyplot as plt
import time
import urllib3
from time import gmtime, strftime
from urllib.request import urlopen
from sklearn.linear_model import LinearRegression

def Rs485_sinReading():    #讀取RS485訊號
    # port name, slave address (in decimal)
    instrument = minimalmodbus.Instrument(comName, 1, mode='rtu')
    # Register number, number of decimals, function code
    idn = instrument.read_register(1, 0, 3)
    locale = instrument.read_register(0, 0, 3)
    wl = (instrument.read_register(0, 0, 4))


    print('id='+str(idn))
    print('location='+str(locale))
    print('RS_value='+str(wl))
    print('------------------------')

    return wl

def waterlevReading():    #零點換算水位
    # port name, slave address (in decimal)
    instrument = minimalmodbus.Instrument(comName, 1, mode='rtu')
    # Register number, number of decimals, function code
    idn = instrument.read_register(1, 0, 3)
    locale = instrument.read_register(0, 0, 3)
    wl = (instrument.read_register(0, 0, 4) -instrument.read_register(0, 0, 4))/1000*26.5/18.8    
    print('water level='+str(wl)+' m')
    print('------------------------')
    time.sleep(0.5)
    return wl

def waterlevReading_real():    #讀取訊號後換算水位
    # port name, slave address (in decimal)
    instrument = minimalmodbus.Instrument(comName, 1, mode='rtu')
    # Register number, number of decimals, function code
    idn = instrument.read_register(1, 0, 3)
    locale = instrument.read_register(0, 0, 3)
    wl = (instrument.read_register(0, 0, 4) -rs_value[0])/1000*26.5/18.8    
    time.sleep(0.5)
    return wl
  
def loop_fun1(): #零點校正用
    for i in range(20):
        print(i+1)#第幾次
        x.append(Rs485_sinReading())
        b.append(waterlevReading())
    rs_value.append(np.median(x))
    true_value.append(np.median(b))
    
def loop_fun2(): #濾定水位用
    for i in range(20):
        print(i+1)#第幾次
        x.append(Rs485_sinReading())
        b.append(waterlevReading_real())
    rs_value.append(np.median(x))
    true_value.append(np.median(b))

def sec_step_fun():
    print('進入第二階段----濾定水位')
    for i in range(3):
        print(i+1)#第幾次
        realin.append(input('輸入現在水位:'))
        loop_fun2()
