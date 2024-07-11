from conexionDB import obtener_conexion, cerrar_conexion

def actualizar_bd():
    conn = obtener_conexion()
    if conn:
        try:
            cursor = conn.cursor()
            
            # Actualizar la base de datos
            cursor.execute("ALTER DATABASE bd_notas CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;")
            
            # Actualizar las tablas
            cursor.execute("ALTER TABLE usuarios CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;")
            cursor.execute("ALTER TABLE notas CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;")
            
            conn.commit()
            print("Base de datos actualizada exitosamente")
            
        except Exception as e:
            print(f"Error al actualizar la base de datos: {e}")
        
        finally:
            if cursor:
                cursor.close()
            cerrar_conexion(conn)

if __name__ == "__main__":
    actualizar_bd()