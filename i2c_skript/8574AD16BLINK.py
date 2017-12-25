#! /usr/bin/env python
# coding: utf-8



import smbus, time
tt=0.28
bus = smbus.SMBus(1)
address = 0x21 #27
bb=255

def fun(nn):
     aa=bb-nn
     time.sleep(tt)
     bus.write_byte(address, aa)


while True:
  try:
     fun(1)
     fun(2)
     fun(4)
     fun(8)
     fun(16)
     fun(32)
     fun(64)
     fun(128)
     bus.write_byte(address, 0)




     time.sleep(0.5)




  except:
    pass
  time.sleep(tt)

