import sqlite3

def init_db():
    """
    - Conecta (o crea) 'database.db'.
    - Crea tabla 'tasks' con columnas:
        id         → clave primaria autoincremental
        title      → texto de la tarea (no nulo)
        completed  → entero 0/1 indicando estado
    """
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER NOT NULL DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()
    print("✅ Base de datos inicializada.")

if __name__ == '__main__':
    init_db()
