import sqlite3
import os

# Step 1: Set the folder where database will be created
db_folder = r"C:\Users\Krishna\Desktop\litedatabase"
os.makedirs(db_folder, exist_ok=True)  # create folder if it doesn't exist

# Step 2: Define database file path
db_path = os.path.join(db_folder, "college1.db")

# Step 3: Connect to database (creates it if it doesn't exist)
conn = sqlite3.connect(db_path)

# Step 4: Create a cursor to execute SQL
cursor = conn.cursor()

# Step 5: Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
)
""")

# Step 6: Insert sample data
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Radha", 21))
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Krishna", 22))

# Step 7: Commit changes and close connection
conn.commit()
conn.close()

print("Database and table created at:", db_path)
