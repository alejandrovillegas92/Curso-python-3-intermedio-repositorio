import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# %%
conn = sqlite3.connect("Trabajo_final.db")

cursor = conn.cursor()

cursor.execute ("""
    CREATE TABLE IF NOT EXISTS Productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_producto TEXT NOT NULL,
        rating TEXT NOT NULL,
        precio INTEGER,
        fecha_envio TEXT NOT NULL,
        enlaces TEXT NOT NULL
    )
    """)

conn.commit()
conn.close()

class Producto(BaseModel):
    producto:str
    rating:str
    precio:str
    fecha_envio:str
    enlaces:str

@app.get("/")
async def index():
    return {"message": "Bienvenido"}

@app.get("/productos/{id}")
async def mostrar_productos(id:int):
    return {"Trabajo_final":id}

@app.post("/agregar/")
async def agregar_producto(producto:Producto):
    conn = sqlite3.connect('trabajo_final.db')
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO Productos (nombre_producto, rating, precio, fecha_envio, enlaces)
                VALUES (?, ?, ?, ? ,?) """, (producto.producto, producto.rating, producto.precio, producto.fecha_envio, producto.enlaces))

    conn.commit()
    conn.close()

    return {'mensaje': 'Producto agregado exitosamente'}