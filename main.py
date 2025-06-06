from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
 
app = FastAPI()
 
class Todo(BaseModel):
    title: str
    description: str
 
def get_db():
    conn = sqlite3.connect('todos.db')
    return conn
 
@app.post("/todos/")
async def create_todo(todo: Todo):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO todos (title, description) VALUES (?, ?)", (todo.title, todo.description))
    conn.commit()
    conn.close()
    return {"message": "Todo created"}
 
@app.get("/todos/")
async def get_todos():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM todos")
    todos = cursor.fetchall()
    conn.close()
    return {"todos": [{"id": todo[0], "title": todo[1], "description": todo[2]} for todo in todos]}
 
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo: Todo):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE todos SET title = ?, description = ? WHERE id = ?", (todo.title, todo.description, todo_id))
    conn.commit()
    conn.close()
    return {"message": "Todo updated"}
 
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    conn.commit()
    conn.close()
    return {"message": "Todo deleted"}