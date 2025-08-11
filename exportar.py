import db
import pandas as pd
import os

def exportar_todo(archivo_excel):
    carpeta = "exportaciones"
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    ruta_archivo = os.path.join(carpeta, archivo_excel)

    conn = db.conectar()
    tablas = ["empleados", "ventas", "devoluciones", "productos", "pagos"]

    with pd.ExcelWriter(ruta_archivo, engine="openpyxl") as writer:
        for tabla in tablas:
            df = pd.read_sql_query(f"SELECT * FROM {tabla}", conn)
            df.to_excel(writer, sheet_name=tabla, index=False)

    conn.close()
    os.startfile(ruta_archivo)  # Abre el archivo automáticamente en Windows
