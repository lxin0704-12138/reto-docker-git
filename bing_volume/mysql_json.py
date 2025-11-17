import json
import mysql.connector

with open("config.json") as f:
    config = json.load(f)

conexion = mysql.connector.connect(**config)

cursor = conexion.cursor()
cursor.execute("SELECT * FROM coches")
datos = cursor.fetchall()

for coche in datos:
    print(coche)

cursor.close()
conexion.close()
