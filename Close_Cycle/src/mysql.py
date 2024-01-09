import pymysql

# Configura los parámetros de conexión
config = {
    'user': 'marcelinne',
    'password': '121206line',
    'host': '192.168.50.11',
    'database': 'apisaas',
    'port': 3306,  # Puerto predeterminado de MariaDB
}

# Intenta establecer la conexión
try:
    connection = pymysql.connect(**config)
    # Realiza operaciones en la base de datos si la conexión es exitosa
    #Print the coneccion status and the host name
    print(f"Conexión establecida: {connection}")
    #select * from the table users
    with connection.cursor() as cursor:
        sql = "SELECT * FROM empresa"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        
except pymysql.Error as err:
    print(f"Error de conexión: {err}")
finally:
    # Asegúrate de cerrar la conexión, ya sea exitosa o no
    if 'connection' in locals() and connection.open:
        connection.close()
        print("Conexión cerrada.")
