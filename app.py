from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DB = 'database.db'

def get_db_connection():
    """
    - Abre conexión SQLite.
    - row_factory permite acceder a filas como dict: row['title']
    """
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/', methods=['GET', 'POST'])
def index():
   return render_template('index.html')

@app.route('/toggle/<int:task_id>')
def toggle(task_id):
    """
    - Invierte el estado 'completed' de la tarea con id=task_id.
    """
    conn = get_db_connection()
    task = conn.execute(
        'SELECT completed FROM tasks WHERE id = ?',
        (task_id,)
    ).fetchone()

    # Si completed=0 → 1, si 1 → 0
    new_state = 0 if task['completed'] else 1
    conn.execute(
        'UPDATE tasks SET completed = ? WHERE id = ?',
        (new_state, task_id)
    )
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    """
    - Borra la tarea con id=task_id de la tabla 'tasks'.
    """
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    # debug=True recarga el servidor al cambiar código
    app.run(debug=True)
