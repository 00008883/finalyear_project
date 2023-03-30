import sqlite3
# #
# # # Initializing Database connection
conn = sqlite3.connect('Data/detection.db')
c = conn.cursor()
c.execute("Select Count(*) from detections")
print(c.fetchall())

c.close()
conn.close()


