import random
import datetime
import itertools
import time

class Sensor:
  def __iter__(self):
    return self
  
  def __next__(self):
     time.sleep(0.5)
     return random.random()
   
   
   
sensor = Sensor()
timestamps = iter(datetime.datetime.now, None)

for stamp, sensor_value in itertools.islice(zip(timestamps, sensor),10):
  print(stamp, sensor_value)
