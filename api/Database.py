import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

# %%
conn = sqlite3.connect("data.db")

cursor - conn.cursor()

cursos.execute ("""
    CREATE TABLE IF NOT EXIST Datos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL
        edad INTEGER,
        curso TEXT NOT NULL
    )
    """)

conn.commit()
conn.close()

class Datos(BaseModel):
    nombre:str
    edad:int
    curso:str

app = FastAPI()

@app.post("/agregar/")


