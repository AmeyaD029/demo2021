import sqlite3

conn = sqlite3.connect('indus.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS vehicleLogData(
               Target_index INT,
               Target_direction INT,
               Target_speed INT,
               Target_RSSI INT,
               No_Samples INT,
               SpeedLimit INT
               )""")

c.execute("""INSERT INTO vehicleLogData VALUES(1,1,76,121,109,80)""")

conn.commit()
c.close()
conn.close()





