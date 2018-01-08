import sqlite3

connection = sqlite3.connect('books.db')
cursor = connection.cursor()

cursor.execute('''INSERT INTO books VALUES
(3, 'TEST BOOK 3 TO ROLLBACK', 'TEST AUTHOR 3', 2003) ''')
#connection.commit()
connection.rollback()

for row in cursor.execute('SELECT * FROM books'):
    print row


connection.close()
