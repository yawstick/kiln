
client_id = b'esp32_temp_kiln'
topic_sub = b'remote_io'
topic_pub = b'temp_kiln'

import max31856

max = max31856.max31856(csPin,misoPin,mosiPin,clkPin)

def read_kiln():
    thermoTempC = max.readThermocoupleTemp()
    thermoTempF = (thermoTempC * 9.0/5.0) + 32
    kilntemp = (b'{0:3.1f}'.format(thermoTempF))
    return(kilntemp)
 
def sub_cb(topic, msg):
  if topic == b'remote_io' and msg == b'sync':
    kilntemp = read_kiln()  
    print('sync received')
    client.publish(topic_pub, kilntemp)
    print(topic_pub, kilntemp)
  if topic == b'remote_io' and msg == b'kiln on':
    pin2.value(1)
    print('kiln on')
  if topic == b'remote_io' and msg == b'kiln off':
    pin2.value(0)
    print('kiln off')
    
def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))

  print (client_id)
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()
 
try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()    

while True:
  try:
    new_message = client.check_msg()
    time.sleep(2)
  except OSError as e:
    restart_and_reconnect()
