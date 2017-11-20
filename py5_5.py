import cPickle
import sys

class Book(object):
	def __init__(self, title, autor, isbn=None):
		self.title = title
		if self.isISBNCorrect(isbn):
			self.isbn = isbn;
		else:
			raise ValueError("ISBN has to be 10 or 13 digits long")
		self.autor = autor
	def __str__(self):
		if self.isbn is None:
			return '"{}" {}'.format(self.title, self.autor)
		else:
			return '"{}" {} {}'.format(self.title, self.isbn, self.autor)
	def isISBNCorrect(self, isbn):
		return len(str(isbn)) == 13 or len(str(isbn)) == 10 or isbn is None

class Bookshelf(object):
	def __init__(self):
		self.books = list()
	def __repr__(self):
		return "\n".join([str(b) for b in self.books])
	def addBook(self, book):
		if not self.isISBNDuplicate(book.isbn):
			self.books.append(book)
	def isISBNDuplicate(self, isbn):
		return next((b for b in self.books if b.isbn == isbn), None)
	def removeBook(self, book):
		self.books.remove(book);
	def to_file(self, picklefile):
		with open(picklefile, 'wb') as handle:
			cPickle.dump(self.books, handle)
	def load(self, picklefile):
		with open(picklefile, 'rb') as handle:
			self.books = cPickle.load(handle)

bs = Bookshelf()
'''
bs.addBook(Book("ksiazka z numerem isbn", "autor autor", 1234567891))
bs.addBook(Book("ksiazka bez numeru isbn", "autor inny"))
bs.addBook(Book("tytul ksiazki", "autor autor", 1234567892))
bs.to_file(sys.argv[1]);
'''
bs.load(sys.argv[1]);
print bs
