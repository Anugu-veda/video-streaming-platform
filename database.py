import sqlite3

conn = sqlite3.connect("videos.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS videos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT
)
""")

conn.commit()
conn.close()

print("Database Created!")