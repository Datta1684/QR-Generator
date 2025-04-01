-- SQLite
import sqlite3

# Connect to the database
conn = sqlite3.connect("qr_codes.db")
c = conn.cursor()

# Drop the existing table (this will delete all data)
c.execute("DROP TABLE IF EXISTS qr_codes")

# Create a new table with the updated schema
c.execute("""
    CREATE TABLE IF NOT EXISTS qr_codes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        original_url TEXT,
        short_url TEXT,
        qr_image BLOB,
        scans INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        password TEXT,
        expiration_date TIMESTAMP,
        location TEXT
    )
""")

# Commit the changes and close the connection
conn.commit()
conn.close()
