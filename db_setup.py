import sqlite3
 
def create_db():
    conn = sqlite3.connect('todos.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT
    )
    ''')
    conn.commit()
    conn.close()
 
if __name__ == '__main__':
    create_db()