# import sqlite3
# import hashlib

# # Connect to the database
# con = sqlite3.connect("demo.db")
# cursor = con.cursor()

# # Create table with correct syntax
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS image_descriptions (
#     id INTEGER PRIMARY KEY,
#     path TEXT,
#     description TEXT,
#     hash TEXT
# )
# """)

# img_path = "/home/o/github/searchfusion/images/tor.png"
# description = "a photo of a shady guy holding a onion"

# with open(img_path, "rb") as img_file:
#     hash_object = hashlib.md5()
#     hash_object.update(img_file.read())
#     hash_ = hash_object.hexdigest()  # Calculating the hash from the image file

#     insert_query = """
# INSERT INTO image_descriptions (path, description, hash)
# VALUES (?, ?, ?)
# """
#     cursor.execute(insert_query, (img_path, description, hash_))

# # Commit the changes
# con.commit()

# # Close the connection
# cursor.close()
# con.close()


import sqlite3
import hashlib

# Function to compute the MD5 hash of a file
def compute_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Database connection and creation
db_name = "demo.db"
conn = sqlite3.connect(db_name)
c = conn.cursor()

# Create the table
c.execute('''
    CREATE TABLE IF NOT EXISTS image_descriptions (
        path TEXT,
        description TEXT,
        hash TEXT UNIQUE
    )
''')

# File details
file_path = "/home/o/github/searchfusion/images/tor.png"
description = "a photo of a shady guy holding an onion"
file_hash = compute_md5(file_path)

# Upsert the file details into the database
c.execute('''
    INSERT OR REPLACE INTO image_descriptions (path, description, hash)
    VALUES (?, ?, ?)
''', (file_path, description, file_hash))

# Commit and close
conn.commit()
conn.close()
