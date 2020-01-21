import mysql.connector

mydb = mysql.connector.connect(
            host="localhost",
            user="Stuart",
            passwd="Stuart@2812",
            database="pyqt5"
        )

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM esportes")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

