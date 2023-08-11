#%%

import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

#%%
class Producto(BaseModel):
    producto:str
    rating:str
    precio:str
    fecha_envio:str
    enlaces:str

app = FastAPI()

#%%
@app.post("/agregar_productos/")
async def agregar_productos(producto:Producto):
    conn = sqlite3.connect('trabajo_final.db')
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO Productos (nombre_producto, rating, precio, fecha_envio, enlaces)
                VALUES (?, ?, ?, ? ,?) """, (producto.producto, producto.rating, producto.precio, producto.fecha_envio, producto.enlaces))
    conn.commit()
    conn.close()
    return {'mensaje': 'Producto agregado exitosamente'}
#%%
@app.get("/leer_productos/")
async def leer_productos():
    conn = sqlite3.connect('Trabajo_final.db')
    cursor = conn.cursor()
    cursor.execute('SELECT nombre_producto, rating, precio, fecha_envio, enlaces FROM Productos')
    resultados = cursor.fetchall()
    conn.commit()
    conn.close()
    if resultados:
        return [{"nombre_producto": resultado[0], 'rating':resultado[1], 'precio':resultado[2], 'fecha_envio':resultado[3], 'enlaces':resultado[4]} for resultado in resultados]
    else:
        return {'mensaje':'No hay datos en la base de datos'}
# %%
@app.get("/leer_productos/{id}/")
async def leer_producto(id:int):
    conn = sqlite3.connect("Trabajo_final.db")
    cursor = conn.cursor()
    cursor.execute ("SELECT nombre_producto, rating, precio, fecha_envio, enlaces FROM Productos WHERE id=?", (id,))
    resultado =cursor.fetchone()
    conn.commit()
    conn.close()
    if resultado:
        return {"nombre_producto": resultado[0], 'rating':resultado[1], 'precio':resultado[2], 'fecha_envio':resultado[3], 'enlaces':resultado[4]}
    else:
        return {'mensaje':'Datos no encontrados'}
# %%
@app.put("/actualizar_productos/{id}")
async def actualizar_productos(id:int, producto:Producto):
    conn =sqlite3.connect('Trabajo_final.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE Productos SET nombre_producto=?, rating=?, precio=?, fecha_envio=?, enlaces=?, WHERE id=?', (producto.producto, producto.rating, producto.precio, producto.fecha_envio, producto.enlaces, id))
    conn.commit()
    conn.close()
    return {'mensaje':"Datos actualizados exitosamente"}

#%%
@app.delete("/eliminar_productos/{id}/")
async def eliminar_productos(id:int):
    conn = sqlite3.connect('Trabajo_final.db')
    cursor = conn.cursor()
    cursor.execute("DELETE from Productos WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return {'mensaje': 'Datos eliminados exitosamente'}


