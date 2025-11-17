import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lxy20050704.",
    database="coches_db"
)

cursor = conexion.cursor()
cursor.execute("SELECT * FROM coches")
datos = cursor.fetchall()

print("ID  MARCA      MODELO       COLOR     KM      PRECIO")
print("-------------------------------------------------------")

for coche in datos:
    print(f"{coche[0]:<4}{coche[1]:<12}{coche[2]:<12}{coche[3]:<10}{coche[4]:<8}{coche[5]:<10}")

cursor.close()
conexion.close()
