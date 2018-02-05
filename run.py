import MySQLdb
import time
conn = MySQLdb.connect("dspms.mysql.pythonanywhere-services.com", "dspms", "10CH30004", "dspms$cognizant" )

c = conn.cursor()

username = 'Python'
tweet = 'man im so cool'

c.execute("INSERT INTO taula (time, username, tweet) VALUES (%s,%s,%s)",
            (time.time(), username, tweet))

conn.commit()

c.execute("SELECT * FROM taula")

rows = c.fetchall()

for eachRow in rows:
    print(eachRow)
