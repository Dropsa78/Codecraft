# exportar.py
import db
import pandas as pd

def exportar_todo(archivo_excel):
    conn = db.conectar()
    tablas = ["empleados", "ventas", "devoluciones", "productos", "pagos"]

    with pd.ExcelWriter(archivo_excel, engine="openpyxl") as writer:
        for tabla in tablas:
            df = pd.read_sql_query(f"SELECT * FROM {tabla}", conn)
            df.to_excel(writer, sheet_name=tabla, index=False)

    conn.close()
