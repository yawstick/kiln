#PDG 
#program   esp32_rio_temp_therm
import time
from simple import MQTTClient
import ubinascii
import machine
import micropython
import dht
import esp
esp.osdebug(None)

import max31856
csPin = 15
misoPin = 12
mosiPin = 13
clkPin = 14

import network
import gc
from machine import Pin
gc.collect()
import os
sensor = dht.DHT22(Pin(18))

ssid = 'your_networkid'
password = 'your_network_password'
mqtt_server = 'your mqtt server ip address'

station = network.WLAN(network.STA_IF)
station.active(True)
station.config(dhcp_hostname= b'esp32_rio_temp_therm')
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())
#print(station.config.dhcp_hostname())
#pin1 = Pin(14, Pin.OUT)
#pin1.value(0)
pin2 = Pin(27, Pin.OUT)
pin2.value(0)
pin3 = Pin(26, Pin.OUT)
pin3.value(0)
pin4 = Pin(25, Pin.OUT)
pin4.value(0)
pin5 = Pin(17, Pin.OUT)
pin5.value(0)
#pin6 = Pin(12, Pin.OUT)
#pin6.value(1)
pin7 = Pin(32, Pin.OUT)
pin7.value(1)
#pin8 = Pin(13, Pin.OUT)
#pin8.value(1)


