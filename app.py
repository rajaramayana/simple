from flask import Flask, render_template, request, redirect
import sqlite3
import os

# Flask app
app = Flask(__name__)

# Database file
db_file = os.path.join(os.getcwd(), "college1.db")

# Ensure the table exists
def init_db():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER
        )
    """)
    conn.commit()
    conn.close()

init_db()

# Home page - list all students
@app.route('/')
def index():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return render_template('index.html', students=students)

# Add new student
@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    age = request.form['age']
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()
    return redirect('/')

# Delete student
@app.route('/delete/<int:id>')
def delete_student(id):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect('/')

# Update student
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_student(id):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        cursor.execute("UPDATE students SET name=?, age=? WHERE id=?", (name, age, id))
        conn.commit()
        conn.close()
        return redirect('/')
    else:
        cursor.execute("SELECT * FROM students WHERE id=?", (id,))
        student = cursor.fetchone()
        conn.close()
        return render_template('update.html', student=student)

# Run app
if __name__ == "__main__":
    app.run(debug=True)
