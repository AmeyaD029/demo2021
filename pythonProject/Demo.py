#!/usr/bin/env python3

import sqlite3
conn = sqlite3.connect('indus.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS vehicleLogData(
               Target_index INT,
               Target_direction INT,
               Target_speed INT,
               Target_RSSI INT,
               No_Samples INT,
               SpeedLimit INT)""")


byte_sensorData = b'#0,1,22,133,55;1,1,77,121,89\r\n'

data = byte_sensorData.decode()
print(data)

a = data.split(";")
for line in a:
    b = line.split(",")
    ObjectID = b[0]
    if "#" in ObjectID:
        Obj = ObjectID.replace("#", " ")
    else:
        Obj = b[0]

    print("Target_Index: "+Obj)
    Direction = b[1]
    print("Target_Direction: "+Direction)
    Speed = b[2]
    print("Target_Speed: "+Speed)
    ReflectedSignal = b[3]
    print("Target_RSSI: "+ReflectedSignal)
    NoOfSamples = b[4]
    print("No_Samples: "+NoOfSamples)
    maxSpeed = 80

    c.execute('''INSERT INTO vehicleLogData(Target_index,Target_direction,Target_speed,
                 Target_RSSI,No_Samples,SpeedLimit) values(?,?,?,?,?,?)''', (Obj, Direction, Speed,
                                                                             ReflectedSignal, NoOfSamples, maxSpeed))
    print("\n")

conn.commit()
c.close()
conn.close()



