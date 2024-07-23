import sqlite3
import argparse
import os
import sys

def search_db(db_path, query):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Use parameterized queries to avoid SQL injection
    cursor.execute("SELECT path, description FROM image_descriptions WHERE description LIKE ?", (f'%{query}%',))
    results = cursor.fetchall()
    
    conn.close()
    return results

def highlight_text(text, query):
    start = text.lower().find(query.lower())
    if start == -1:
        return text
    end = start + len(query)
    return (
        text[:start] +
        '\033[91m' + text[start:end] + '\033[0m' +
        text[end:]
    )

def format_path(path):
    return '[' + os.path.basename(path) + " ]:"

def main():
    parser = argparse.ArgumentParser(description='Search image descriptions in an SQLite database.')
    parser.add_argument('--db', '-d', required=True, help='Path to the SQLite database file.')
    parser.add_argument('--query', '-q', required=True, help='Search query for descriptions.')
    
    args = parser.parse_args()
    
    if not os.path.isfile(args.db):
        print(f"Error: The database file '{args.db}' does not exist.")
        sys.exit(1)

    results = search_db(args.db, args.query)
    
    if not results:
        print("No results found.")
        return
    
    for path, description in results:
        formatted_path = format_path(path)
        highlighted_description = highlight_text(description, args.query)
        print(f"{formatted_path}, Description: {highlighted_description}")
    end = ""
if __name__ == "__main__":
    main()
