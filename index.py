import mysql.connector

#creando nuestro diccionario
dato={
    'user':'root',
    'password':'',
    'database':'ejemplo',
    'host':'127.0.0.1'
}#diccionario

#establecer conexion
conexion=mysql.connector.connect(** dato)


cursor=conexion.cursor()

valores="insert into usuario(codigo,nombre)values('2','Alexander')"

try:
    cursor.execute(valores)
    conexion.commit()
    print("ingresado valores en la BD")
except:
    print("Valores no ingresados")

conexion.close()
