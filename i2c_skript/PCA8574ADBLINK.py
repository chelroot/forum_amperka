#! /usr/bin/env python
# coding: utf-8


import smbus, time
tt=0.08
bus = smbus.SMBus(1)
address = 0x38

while True:
  try:
#    bus.write_byte(address, 0xEF)
     aa=255-1
     time.sleep(tt)
     bus.write_byte(address, aa)
     aa=255-2
     time.sleep(tt)
     bus.write_byte(address, aa)
     aa=255-4
     time.sleep(tt)
     bus.write_byte(address, aa)
     aa=255-8
     time.sleep(tt)
     bus.write_byte(address, aa)
     aa=255-16
     time.sleep(tt)
     bus.write_byte(address, aa)
     aa=255-32
     time.sleep(tt)
     bus.write_byte(address, aa)
     aa=255-64
     time.sleep(tt)
     bus.write_byte(address, aa)
     aa=255-128
     time.sleep(tt)
     bus.write_byte(address, aa)

#@     bus.write_byte(address, 2)
#     bus.write_byte(address, 3)
#     bus.write_byte(address, 4)
  except:
    pass
  time.sleep(tt)
  try:
    bus.write_byte(address, 255)
  except:
    pass
  time.sleep(tt)


