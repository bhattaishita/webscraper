import sqlite3
def create_database():
    """
    Creates a SQLite database with a table to store book information.
    """
    conn = sqlite3.connect("book.db")  
    cursor = conn.cursor()
    
    # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS book (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_title TEXT NOT NULL,
            book_url XT NOT NULL,
            rating TEXT
           
        )
    ''')
    
    conn.commit()
    conn.close()

create_database()

def insert_book_data(book_title, book_url, rating):
    """
    Inserts book data into the database.
    """
    conn = sqlite3.connect("book.db")
    cursor = conn.cursor()

    cursor.execute('''
        SELECT COUNT(*) FROM book WHERE book_title= ?
    ''', (book_title,))

    result = cursor.fetchone()
    if result[0] >0:
        print('Already Exists')
        return

    
    cursor.execute('''
        INSERT INTO book ('book_title', 'book_url', 'rating')
        VALUES (?, ?, ?)
    ''', (book_title, book_url, rating))
    
    conn.commit()
    conn.close()
    print(f"Data inserted: {book_title}" )
    print(f"Data inserted:  { book_url}" )
    print(f"Data inserted:  {rating}")