# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 18:36:10 2019

@author: Luming
"""
#模組輸入
import minimalmodbus
import numpy as np
import time
import urllib3
from time import gmtime, strftime
from urllib.request import urlopen
from sklearn.linear_model import LinearRegression
import modbus_reading #副程式
import matplotlib.pyplot as plt
#參數設定
minimalmodbus.BAUDRATE = 19200
devName = '/dev/ttyUSB0' # RPI    format
comName = 'COM4'        # Window format
id_No = "6999"

#設定變數
rs_value = [] #擷取的結果(rs485)
true_value = [] #擷取後換算水位結果
x = [] #迴圈中讀到的值(RS485)暫存
b = [] #迴圈中計算的值(水位)暫存
realin = []
rs_np =[]
tr_np =[]
#開始流程
a = input('是否要進入零點校正(Yes or no):')

#判斷式(第一階段:零點校正,第二階段:水位濾定
if a.lower() == 'yes' :
    print('開始零點校正')
    loop_fun1()
   sec_step_fun()
elif a.lower() == 'no':
    sec_step_fun()
else:
    print('請重新跑過')

#取值計算回歸式
tr_value=np.array(true_value)
realin_np=np.array(realin)

Tr_np=tr_np.reshape(tr_value,(len(tr_value),1))
Realin_np=realin_np.reshape(realin,(len(realin),1))
regr = LinearRegression()
print(regr.fit(Rs_np,Tr_np))
print(regr.coef_) #係數
print(Tr_np=regr.coef_*Rs_np+regr.intercept_) #截距

#判斷是否符合R^2>0.95

if regr.coef_ >=0.95:
    print('結束校正')
else :
    sec_step_fun()



