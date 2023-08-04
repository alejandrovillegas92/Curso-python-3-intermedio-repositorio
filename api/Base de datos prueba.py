import sqlite3

conn = sqlite3.connect("prueba.db")

cursor = conn.cursor()

cursor.execute ("""CREATE TABLE IF NOT EXIST Usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    edad INTEGER) """)

conn.commit()
conn.close()
