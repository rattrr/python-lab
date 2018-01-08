import sqlite3

connection = sqlite3.connect('books.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS
books (id integer, title text, author text, year integer)''')
cursor.execute('''INSERT INTO books VALUES
(2, 'TEST BOOK 2', 'TEST AUTHOR 2', 2001) ''')

connection.commit()

cursor.execute(''' DELETE FROM books WHERE id=2 ''')
cursor.execute(''' UPDATE books SET title="updated title" WHERE id=1''')

for row in cursor.execute('SELECT * FROM books'):
    print row


connection.close()
