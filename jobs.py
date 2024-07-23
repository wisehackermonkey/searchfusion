# # import os
# # import hashlib
# # import sqlite3
# # import subprocess
# # # import time
# # from queue import PriorityQueue
# # from threading import Thread
# # from pathlib import Path

# # # Configuration
# # images = ['png', 'jpg', 'gif', 'webp', 'bmp']
# # NUMWORKERS = 2
# # DB_FILE = 'jobs.db'
# # TABLE_NAME = 'jobs_queue'

# # # Initialize SQLite database
# # def init_db():
# #     conn = sqlite3.connect(DB_FILE)
# #     c = conn.cursor()
# #     c.execute(f'''
# #     CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
# #         path TEXT PRIMARY KEY,
# #         time INTEGER,
# #         hash TEXT UNIQUE,
# #         completed BOOLEAN
# #     )
# #     ''')
# #     conn.commit()
# #     conn.close()

# # # Calculate file hash
# # def file_hash(file_path):
# #     hasher = hashlib.sha256()
# #     with open(file_path, 'rb') as f:
# #         buf = f.read(8192)
# #         while len(buf) > 0:
# #             hasher.update(buf)
# #             buf = f.read(8192)
# #     return hasher.hexdigest()

# # # Add job to the database
# # def add_job(file_path):
# #     conn = sqlite3.connect(DB_FILE)
# #     c = conn.cursor()
# #     file_hash_value = file_hash(file_path)
# #     c.execute(f'''
# #     INSERT OR IGNORE INTO {TABLE_NAME} (path, time, hash, completed)
# #     VALUES (?, ?, ?, ?)
# #     ''', (file_path, int(os.path.getmtime(file_path)), file_hash_value, False))
# #     conn.commit()
# #     conn.close()

# # # Discover images in the specified directories
# # def discover_images(directories):
# #     for directory in directories:
# #         for root, _, files in os.walk(directory):
# #             for file in files:
# #                 if file.split('.')[-1].lower() in images:
# #                     add_job(os.path.join(root, file))

# # # Fetch jobs from the database
# # def fetch_jobs():
# #     conn = sqlite3.connect(DB_FILE)
# #     c = conn.cursor()
# #     c.execute(f'''
# #     SELECT path FROM {TABLE_NAME}
# #     WHERE completed = 0
# #     ''')
# #     jobs = c.fetchall()
# #     conn.close()
# #     return jobs

# # # Mark job as completed
# # def mark_as_completed(file_path):
# #     conn = sqlite3.connect(DB_FILE)
# #     c = conn.cursor()
# #     c.execute(f'''
# #     UPDATE {TABLE_NAME}
# #     SET completed = 1
# #     WHERE path = ?
# #     ''', (file_path,))
# #     conn.commit()
# #     conn.close()

# # # Worker function
# # def worker():
# #     while True:
# #         job = queue.get()
# #         if job is None:
# #             break
# #         file_path = job
# #         subprocess.run(['python', 'blip.py', '--text', 'photo of', '--verbose', '--input_file', file_path])
# #         mark_as_completed(file_path)
# #         queue.task_done()

# # # Main script
# # if __name__ == "__main__":
# #     init_db()
    
# #     # Example usage: Update with your directories
# #     directories_to_search = ['./images', './secret']
# #     discover_images(directories_to_search)

# #     jobs = fetch_jobs()
    
# #     # Create a priority queue and start workers
# #     queue = PriorityQueue()
# #     threads = []
# #     for _ in range(NUMWORKERS):
# #         t = Thread(target=worker)
# #         t.start()
# #         threads.append(t)
    
# #     # Add jobs to the queue
# #     for job in jobs:
# #         queue.put(job[0])
    
# #     # Stop workers
# #     queue.join()
# #     for _ in range(NUMWORKERS):
# #         queue.put(None)
# #     for t in threads:
# #         t.join()
# import os
# import hashlib
# import sqlite3
# import subprocess
# from pathlib import Path
# from queue import Queue
# from threading import Thread

# # Configuration
# images_ext = ['png', 'jpg', 'gif', 'webp', 'bmp']
# NUMWORKERS = 2
# DB_JOB_FILE = 'jobs.db'
# DB_DESC_FILE = 'images.db'
# TABLE_JOB_NAME = 'jobs_queue'
# TABLE_DESC_NAME = 'image_descriptions'

# # Initialize SQLite databases
# def init_db():
#     conn = sqlite3.connect(DB_JOB_FILE)
#     c = conn.cursor()
#     c.execute(f'''
#     CREATE TABLE IF NOT EXISTS {TABLE_JOB_NAME} (
#         path TEXT PRIMARY KEY,
#         time INTEGER,
#         hash TEXT UNIQUE,
#         completed BOOLEAN
#     )
#     ''')
#     conn.commit()
#     conn.close()

#     conn = sqlite3.connect(DB_DESC_FILE)
#     c = conn.cursor()
#     c.execute(f'''
#     CREATE TABLE IF NOT EXISTS {TABLE_DESC_NAME} (
#         path TEXT,
#         description TEXT,
#         hash TEXT UNIQUE PRIMARY KEY
#     )
#     ''')
#     conn.commit()
#     conn.close()

# # Calculate file hash
# def file_hash(file_path):
#     hasher = hashlib.sha256()
#     with open(file_path, 'rb') as f:
#         buf = f.read(8192)
#         while len(buf) > 0:
#             hasher.update(buf)
#             buf = f.read(8192)
#     return hasher.hexdigest()

# # Add job to the database
# def add_job(file_path):
#     conn = sqlite3.connect(DB_JOB_FILE)
#     c = conn.cursor()
#     file_hash_value = file_hash(file_path)
#     c.execute(f'''
#     INSERT OR IGNORE INTO {TABLE_JOB_NAME} (path, time, hash, completed)
#     VALUES (?, ?, ?, ?)
#     ''', (file_path, int(os.path.getmtime(file_path)), file_hash_value, False))
#     conn.commit()
#     conn.close()

# # Discover images in the specified directories
# def discover_images(directories):
#     for directory in directories:
#         for root, _, files in os.walk(directory):
#             for file in files:
#                 if file.split('.')[-1].lower() in images_ext:
#                     add_job(os.path.join(root, file))

# # Fetch jobs from the database
# def fetch_jobs():
#     conn = sqlite3.connect(DB_JOB_FILE)
#     c = conn.cursor()
#     c.execute(f'''
#     SELECT path FROM {TABLE_JOB_NAME}
#     WHERE completed = 0
#     ''')
#     jobs = c.fetchall()
#     conn.close()
#     return jobs

# # Mark job as completed
# def mark_as_completed(file_path):
#     conn = sqlite3.connect(DB_JOB_FILE)
#     c = conn.cursor()
#     c.execute(f'''
#     UPDATE {TABLE_JOB_NAME}
#     SET completed = 1
#     WHERE path = ?
#     ''', (file_path,))
#     conn.commit()
#     conn.close()

# # Store description into the database
# def store_description(file_path, description):
#     file_hash_value = file_hash(file_path)
#     conn = sqlite3.connect(DB_DESC_FILE)
#     c = conn.cursor()
#     c.execute(f'''
#     INSERT OR REPLACE INTO {TABLE_DESC_NAME} (path, description, hash)
#     VALUES (?, ?, ?)
#     ''', (file_path, description, file_hash_value))
#     conn.commit()
#     conn.close()

# # Worker function
# def worker():
#     while True:
#         file_path = queue.get()
#         if file_path is None:
#             break
#         result = subprocess.run(['python', 'blip.py', '--text', 'photo of', '--verbose', '--input_file', file_path], capture_output=True, text=True)
#         store_description(file_path, result.stdout)
#         mark_as_completed(file_path)
#         queue.task_done()

# # Main script
# if __name__ == "__main__":
#     init_db()

#     # Example usage: Update with your directories
#     directories_to_search = ['./images', './secret']
#     discover_images(directories_to_search)

#     jobs = fetch_jobs()

#     # Create a queue and start workers
#     queue = Queue()
#     threads = []
#     for _ in range(NUMWORKERS):
#         t = Thread(target=worker)
#         t.start()
#         threads.append(t)

#     # Add jobs to the queue
#     for job in jobs:
#         queue.put(job[0])

#     # Stop workers
#     queue.join()
#     for _ in range(NUMWORKERS):
#         queue.put(None)
#     for t in threads:
#         t.join()
import os
import hashlib
import sqlite3
import subprocess
from pathlib import Path
from queue import Queue
from threading import Thread

# Configuration
images_ext = ['png', 'jpg', 'gif', 'webp', 'bmp']
NUMWORKERS = 2
DB_JOB_FILE = 'jobs.db'
DB_DESC_FILE = 'images.db'
TABLE_JOB_NAME = 'jobs_queue'
TABLE_DESC_NAME = 'image_descriptions'

# Initialize SQLite databases
def init_db():
    conn = sqlite3.connect(DB_JOB_FILE)
    c = conn.cursor()
    c.execute(f'''
    CREATE TABLE IF NOT EXISTS {TABLE_JOB_NAME} (
        path TEXT PRIMARY KEY,
        time INTEGER,
        hash TEXT UNIQUE,
        completed BOOLEAN
    )
    ''')
    conn.commit()
    conn.close()

    conn = sqlite3.connect(DB_DESC_FILE)
    c = conn.cursor()
    c.execute(f'''
    CREATE TABLE IF NOT EXISTS {TABLE_DESC_NAME} (
        path TEXT,
        description TEXT,
        hash TEXT UNIQUE PRIMARY KEY
    )
    ''')
    conn.commit()
    conn.close()

# Calculate file hash
def file_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        buf = f.read(8192)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(8192)
    return hasher.hexdigest()

# Add job to the database
def add_job(file_path):
    conn = sqlite3.connect(DB_JOB_FILE)
    c = conn.cursor()
    file_hash_value = file_hash(file_path)
    c.execute(f'''
    INSERT OR IGNORE INTO {TABLE_JOB_NAME} (path, time, hash, completed)
    VALUES (?, ?, ?, ?)
    ''', (file_path, int(os.path.getmtime(file_path)), file_hash_value, False))
    conn.commit()
    conn.close()

# Discover images in the specified directories
def discover_images(directories):
    for directory in directories:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.split('.')[-1].lower() in images_ext:
                    add_job(os.path.join(root, file))

# Fetch jobs from the database
def fetch_jobs():
    conn = sqlite3.connect(DB_JOB_FILE)
    c = conn.cursor()
    c.execute(f'''
    SELECT path FROM {TABLE_JOB_NAME}
    WHERE completed = 0
    ''')
    jobs = c.fetchall()
    conn.close()
    return jobs

# Mark job as completed
def mark_as_completed(file_path):
    conn = sqlite3.connect(DB_JOB_FILE)
    c = conn.cursor()
    c.execute(f'''
    UPDATE {TABLE_JOB_NAME}
    SET completed = 1
    WHERE path = ?
    ''', (file_path,))
    conn.commit()
    conn.close()

# Store description into the database
def store_description(file_path, description):
    file_hash_value = file_hash(file_path)
    conn = sqlite3.connect(DB_DESC_FILE)
    c = conn.cursor()
    c.execute(f'''
    INSERT OR REPLACE INTO {TABLE_DESC_NAME} (path, description, hash)
    VALUES (?, ?, ?)
    ''', (file_path, description, file_hash_value))
    conn.commit()
    conn.close()

# Worker function
def worker():
    while True:
        file_path = queue.get()
        if file_path is None:
            break
        result = subprocess.run(['python', 'blip.py', '--text', 'photo of', '--input_file', file_path], capture_output=True, text=True)
        results[file_path] = result.stdout
        queue.task_done()

# Main script
if __name__ == "__main__":
    init_db()

    # Example usage: Update with your directories
    directories_to_search = ['./images']
    discover_images(directories_to_search)

    jobs = fetch_jobs()

    # Create a queue and start workers
    queue = Queue()
    threads = []
    results = {}

    for _ in range(NUMWORKERS):
        t = Thread(target=worker)
        t.start()
        threads.append(t)

    # Add jobs to the queue
    for job in jobs:
        queue.put(job[0])

    # Stop workers
    queue.join()
    for _ in range(NUMWORKERS):
        queue.put(None)
    for t in threads:
        t.join()

    # Store results and mark jobs as completed
    for file_path, description in results.items():
        store_description(file_path, description)
        mark_as_completed(file_path)
