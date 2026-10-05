from fastapi import FastAPI, HTTPException
from con_db import obtener_conexion

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API Sentir - FastAPI"}

# ==========================================
# PERSONAS (Código original del profesor)
# ==========================================
@app.get("/personas")
def consultar_personas():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT id_persona, nombre, telefono, tipo_persona FROM personas")
    personas = cursor.fetchall()
    cursor.close()
    conexion.close()
    return personas

@app.post("/personas")
def guardar_persona(persona: dict):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO personas (nombre, telefono, tipo_persona)
        VALUES (%s, %s, %s)
    """, (persona["nombre"], persona["telefono"], persona["tipo_persona"]))
    conexion.commit()
    cursor.close()
    conexion.close()
    return {"message": "Persona guardada correctamente"}

@app.put("/personas/{id_persona}")
def actualizar_persona(id_persona: int, persona: dict):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE personas
        SET nombre = %s, telefono = %s, tipo_persona = %s
        WHERE id_persona = %s
    """, (persona["nombre"], persona["telefono"], persona["tipo_persona"], id_persona))
    conexion.commit()
    cursor.close()
    conexion.close()
    return {"message": "Persona actualizada correctamente"}

@app.delete("/personas/{id_persona}")
def eliminar_persona(id_persona: int):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM personas WHERE id_persona = %s", (id_persona,))
    conexion.commit()
    cursor.close()
    conexion.close()
    return {"message": "Persona eliminada correctamente"}

# ==========================================
# EMERGENCIAS
# ==========================================
@app.get("/emergencias")
def consultar_emergencias():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT id_emergencia, tipo, descripcion, fecha, estado, id_persona FROM emergencias")
    emergencias = cursor.fetchall()
    cursor.close()
    conexion.close()
    return emergencias

@app.get("/emergencias/{id_emergencia}")
def consultar_emergencia(id_emergencia: int):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM emergencias WHERE id_emergencia = %s", (id_emergencia,))
    emergencia = cursor.fetchone()
    cursor.close()
    conexion.close()
    if not emergencia:
        raise HTTPException(status_code=404, detail="Emergencia no encontrada")
    return emergencia

@app.post("/emergencias")
def guardar_emergencia(emergencia: dict):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO emergencias (tipo, descripcion, estado, id_persona)
        VALUES (%s, %s, %s, %s)
    """, (emergencia["tipo"], emergencia["descripcion"], emergencia["estado"], emergencia["id_persona"]))
    conexion.commit()
    cursor.close()
    conexion.close()
    return {"message": "Emergencia registrada correctamente"}

@app.put("/emergencias/{id_emergencia}")
def actualizar_emergencia(id_emergencia: int, emergencia: dict):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE emergencias
        SET tipo = %s, descripcion = %s, estado = %s
        WHERE id_emergencia = %s
    """, (emergencia["tipo"], emergencia["descripcion"], emergencia["estado"], id_emergencia))
    if cursor.rowcount == 0:
        cursor.close()
        conexion.close()
        raise HTTPException(status_code=404, detail="Emergencia no encontrada")
    conexion.commit()
    cursor.close()
    conexion.close()
    return {"message": "Emergencia actualizada correctamente"}

@app.delete("/emergencias/{id_emergencia}")
def eliminar_emergencia(id_emergencia: int):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM emergencias WHERE id_emergencia = %s", (id_emergencia,))
    if cursor.rowcount == 0:
        cursor.close()
        conexion.close()
        raise HTTPException(status_code=404, detail="Emergencia no encontrada")
    conexion.commit()
    cursor.close()
    conexion.close()
    return {"message": "Emergencia eliminada correctamente"}

# ==========================================
# UBICACIONES
# ==========================================
@app.get("/ubicaciones")
def consultar_ubicaciones():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT id_ubicacion, latitud, longitud, direccion, id_emergencia FROM ubicaciones")
    ubicaciones = cursor.fetchall()
    cursor.close()
    conexion.close()
    return ubicaciones

@app.get("/ubicaciones/{id_ubicacion}")
def consultar_ubicacion(id_ubicacion: int):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM ubicaciones WHERE id_ubicacion = %s", (id_ubicacion,))
    ubicacion = cursor.fetchone()
    cursor.close()
    conexion.close()
    if not ubicacion:
        raise HTTPException(status_code=404, detail="Ubicación no encontrada")
    return ubicacion

@app.post("/ubicaciones")
def guardar_ubicacion(ubicacion: dict):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO ubicaciones (latitud, longitud, direccion, id_emergencia)
        VALUES (%s, %s, %s, %s)
    """, (ubicacion["latitud"], ubicacion["longitud"], ubicacion["direccion"], ubicacion["id_emergencia"]))
    conexion.commit()
    cursor.close()
    conexion.close()
    return {"message": "Ubicación registrada correctamente"}

@app.put("/ubicaciones/{id_ubicacion}")
def actualizar_ubicacion(id_ubicacion: int, ubicacion: dict):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE ubicaciones
        SET latitud = %s, longitud = %s, direccion = %s
        WHERE id_ubicacion = %s
    """, (ubicacion["latitud"], ubicacion["longitud"], ubicacion["direccion"], id_ubicacion))
    if cursor.rowcount == 0:
        cursor.close()
        conexion.close()
        raise HTTPException(status_code=404, detail="Ubicación no encontrada")
    conexion.commit()
    cursor.close()
    conexion.close()
    return {"message": "Ubicación actualizada correctamente"}

@app.delete("/ubicaciones/{id_ubicacion}")
def eliminar_ubicacion(id_ubicacion: int):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM ubicaciones WHERE id_ubicacion = %s", (id_ubicacion,))
    if cursor.rowcount == 0:
        cursor.close()
        conexion.close()
        raise HTTPException(status_code=404, detail="Ubicación no encontrada")
    conexion.commit()
    cursor.close()
    conexion.close()
    return {"message": "Ubicación eliminada correctamente"}

# ==========================================
# INTEGRACIÓN
# ==========================================
@app.get("/emergencias/{id_emergencia}/ubicacion")
def consultar_ubicacion_emergencia(id_emergencia: int):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM ubicaciones WHERE id_emergencia = %s", (id_emergencia,))
    ubicacion = cursor.fetchone()
    cursor.close()
    conexion.close()
    if not ubicacion:
        raise HTTPException(status_code=404, detail="Ubicación no encontrada para esta emergencia")
    return ubicacion

@app.get("/emergencias/{id_emergencia}/detalle")
def consultar_detalle_emergencia(id_emergencia: int):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT e.id_emergencia, e.tipo, e.descripcion, e.estado, 
               p.nombre, p.telefono, 
               u.direccion, u.latitud, u.longitud
        FROM emergencias e
        INNER JOIN personas p ON e.id_persona = p.id_persona
        LEFT JOIN ubicaciones u ON e.id_emergencia = u.id_emergencia
        WHERE e.id_emergencia = %s
    """, (id_emergencia,))
    detalle = cursor.fetchone()
    cursor.close()
    conexion.close()
    if not detalle:
        raise HTTPException(status_code=404, detail="Emergencia no encontrada")
        
    return {
        "id_emergencia": detalle[0],
        "tipo": detalle[1],
        "descripcion": detalle[2],
        "estado": detalle[3],
        "reportado_por": {
            "nombre": detalle[4],
            "telefono": detalle[5]
        },
        "ubicacion": {
            "direccion": detalle[6],
            "latitud": detalle[7],
            "longitud": detalle[8]
        } if detalle[6] else "Sin ubicación asignada"
    }