import mysql.connector

conexion = mysql.connector.connect (
    host = "localhost",
    port = 3306,
    user = "root",
    password = "12345",
    db = "conecta_materiales"
)