import sqlite3
import csv

def crear_tabla():
    conn = sqlite3.connect('Trabajo_final.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_producto TEXT NOT NULL,
        rating TEXT NOT NULL,
        precio INTEGER,
        fecha_envio TEXT NOT NULL,
        enlaces TEXT NOT NULL)''')  

    conn.commit()
    conn.close()

def leer_csv(csv_file):
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

def insertar_datos_tabla(data):
    conn = sqlite3.connect('Trabajo_final.db')
    cursor = conn.cursor()

    for row in data:
        cursor.execute('''INSERT INTO Productos (nombre_producto, rating, precio, fecha_envio, enlaces)
                       VALUES (?,?,?,?,?) ''', (row['Productos'], row['Rating'], row['Precio'], row['Fecha de envio'], row['Enlaces']))
    
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    csv_file = r'C:\Users\cross\OneDrive\Escritorio\Aprendiendo Python 3 Intermedio\Curso python 3 intermedio repositorio\Trabajo_Final\Trabajo_Final_Alejandro_Villegas05-08-2023.csv'
    crear_tabla()  
    insertar_datos = leer_csv(csv_file)
    insertar_datos_tabla(insertar_datos)

