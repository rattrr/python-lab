class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return "Book: {}, Author: {}".format(self.title, self.author)

class CD(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return "CD: {}, Author: {}".format(self.title, self.author)

class Collections(object):
    def __init__(self):
        self.books = list()
        self.cds = list()
    def __str__(self):
        return "\n\nBooks:\n{}\n\nCDs:\n{}\n".format("\n".join([str(book) for book in self.books]), "\n".join([str(cd) for cd in self.cds]))
    def add(self, item):
        if(type(item) is Book):
            self.books.append(item)
        if(type(item) is CD):
            self.cds.append(item)
    def update(self, item, attribute, newValue):
        if attribute == "title":
            item.title = newValue
        elif attribute == "author":
            item.author = newValue
    def remove(self, item):
        if(type(item) is Book):
            self.books.remove(item)
        if(type(item) is CD):
            self.cds.remove(item)
    def getAllItemsOfType(self, type):
        if type == "books":
            return "\n".join([str(book) for book in self.books])
        if type == "cds":
            return "\n".join([str(cd) for cd in self.cds])
    def filter(self, attribute = None, value = None):
        if attribute is None and value is None:
            return self
        elif attribute == "title":
            return [str(x) for x in self.books if x.title == value] + [str(x) for x in self.cds if x.title == value]
        elif attribute == "author":
            return [str(x) for x in self.books if x.author == value] + [str(x) for x in self.cds if x.author == value]

collection = Collections()
b1 = Book("book 1", "author 1")
b2 = Book("book 2", "author 2")
b3 = Book("book 3", "author 3")
c1 = CD("cd1", "author 1")
collection.add(b1)
collection.add(b2)
collection.add(b3)
collection.add(c1)
collection.remove(b2)
collection.update(c1, "title", "updated title")

print collection.getAllItemsOfType("books")
print collection.filter()
print collection.filter("author", "author 1")
