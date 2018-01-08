import sqlite3

connection = sqlite3.connect('books.db')
cursor = connection.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS person(pid INTEGER PRIMARY KEY, name text,
FOREIGN KEY (bookid) REFERENCES books(id))''')

#cursor.execute('''INSERT INTO person VALUES
#(1, 'some name idk') ''')

#connection.commit()


for row in cursor.execute('SELECT * FROM books INNER JOIN person'):
    print row


connection.close()
