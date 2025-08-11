# db.py
import sqlite3

def conectar():
    conn = sqlite3.connect('pymes_app.db')
    return conn

def crear_tablas():
    conn = conectar()
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS empleados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        puesto TEXT NOT NULL,
        salario REAL NOT NULL
    )
    """)
    c.execute("""
    CREATE TABLE IF NOT EXISTS ventas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        producto TEXT NOT NULL,
        cantidad INTEGER NOT NULL,
        precio_unitario REAL NOT NULL,
        total REAL NOT NULL
    )
    """)
    c.execute("""
    CREATE TABLE IF NOT EXISTS devoluciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        producto TEXT NOT NULL,
        cantidad INTEGER NOT NULL,
        motivo TEXT
    )
    """)
    c.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL,
        stock INTEGER NOT NULL
    )
    """)
    c.execute("""
    CREATE TABLE IF NOT EXISTS pagos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        proveedor TEXT NOT NULL,
        monto REAL NOT NULL,
        fecha TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def insertar_empleado(nombre, puesto, salario):
    conn = conectar()
    c = conn.cursor()
    c.execute("INSERT INTO empleados (nombre, puesto, salario) VALUES (?, ?, ?)",
              (nombre, puesto, salario))
    conn.commit()
    conn.close()

def obtener_empleados():
    conn = conectar()
    c = conn.cursor()
    c.execute("SELECT * FROM empleados")
    datos = c.fetchall()
    conn.close()
    return datos

def eliminar_empleado(id):
    conn = conectar()
    c = conn.cursor()
    c.execute("DELETE FROM empleados WHERE id = ?", (id,))
    conn.commit()
    conn.close()
