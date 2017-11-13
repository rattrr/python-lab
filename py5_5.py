import cPickle
import sys

picklefile = sys.argv[1]

def Book(object):
	def __init__(self, title, isbn, autor):
		self.title = title
		self.isbn = isbn
		self.autor = autor
	def __repr__(self):
		return "{} {} {}".format(self.tittle, self.isbn, self.autor)

def Bookshelf(object):
	def __init__(self):
		self.books = list()
	def addBook(self, book):
		self.books.append(book)
	def to_file(self):
		with open(picklefile, 'wb') as handle:
			cPickle.dump(self.books, handle, protocol=pickle.HIGHEST_PROTOCOL)
	def load(self):
		with open(picklefile, 'rb') as handle:
			self.books = cPickle.load()

bs = Bookshelf()

