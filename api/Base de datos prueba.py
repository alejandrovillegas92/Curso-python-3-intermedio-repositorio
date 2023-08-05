import sqlite3

conn = sqlite3.connect("prueba.db")

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT NOT NULL,
               edad INTEGER
)''')

conn.commit()
conn.close()

conn = sqlite3.connect("prueba.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("Juan", 21))

conn.commit()
cursor.close()
conn.close()

from fastapi import FastAPI
from pydantic import BaseModel

