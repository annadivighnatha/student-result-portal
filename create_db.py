import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("students.db")

# Create a cursor
cursor = conn.cursor()

# Create Student table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    hall_ticket TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    branch TEXT NOT NULL,
    semester TEXT NOT NULL,
    python INTEGER,
    java INTEGER,
    dbms INTEGER,
    web INTEGER,
    cgpa REAL
)
""")

# Insert 10 student records
students = [
    ("22691A0501", "Rahul",   "CSE", "IV-I", 90, 85, 88, 92, 8.88),
    ("22691A0502", "Priya",   "CSE", "IV-I", 95, 91, 89, 90, 9.10),
    ("22691A0503", "Arjun",   "CSE", "IV-I", 80, 82, 78, 85, 8.20),
    ("22691A0504", "Sneha",   "CSE", "IV-I", 92, 88, 91, 94, 9.02),
    ("22691A0505", "Kiran",   "CSE", "IV-I", 75, 80, 79, 82, 7.95),
    ("22691A0506", "Anjali",  "CSE", "IV-I", 89, 90, 87, 91, 8.90),
    ("22691A0507", "Vikram",  "CSE", "IV-I", 84, 86, 85, 88, 8.55),
    ("22691A0508", "Meghana", "CSE", "IV-I", 91, 93, 92, 95, 9.25),
    ("22691A0509", "Rohit",   "CSE", "IV-I", 78, 76, 81, 80, 8.05),
    ("22691A0510", "Deepika", "CSE", "IV-I", 94, 92, 90, 93, 9.15)
]

cursor.executemany("""
INSERT OR REPLACE INTO students
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", students)

# Save changes
conn.commit()

# Close connection
conn.close()

print("Database created successfully!")