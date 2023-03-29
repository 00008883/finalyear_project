import sqlite3
import datetime

# Initializing Database connection
conn = sqlite3.connect('Data/detection.db')
c = conn.cursor()

# Initializes table if does not exist
createTable = '''
          CREATE TABLE IF NOT EXISTS detections
          ([forehead] INTEGER, [eye] INTEGER, [chest] INTEGER, [DetectionDate] TIMESTAMP)
          '''
c.execute(createTable)

# Number of rows in the current state
count = "SELECT COUNT(*) FROM detections"
c.execute(count)
# Assign value to initial_rows variable
initial_rows = c.fetchone()[0]


def InsertData(detections):
    # Getting current time
    currentTime = datetime.datetime.now()
    insertQuery = "INSERT INTO detections VALUES (?, ?, ?, ?)"
    # Executing insertQuery statement to insert detected values into the table
    c.execute(insertQuery, (detections[0], detections[1], detections[2], currentTime))
    conn.commit()
    #c.execute("DROP TABLE detections")

    #c.execute("SELECT * FROM detections")
    #print(c.fetchall())


def GetDetection():
    # Statement which selects last row from table
    selectLast = "SELECT * FROM detections ORDER BY DetectionDate DESC LIMIT 1"
    c.execute(selectLast)
    detection = c.fetchone()
    return detection
