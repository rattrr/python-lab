from django.db import models

class Book(models.Model):
    isbn = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year = models.IntegerField()
    def __str__(self):
        return "{} {} {} {}".format(self.isbn, self.title, self.author, self.year)

class Reader(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        return str(self.id) + " " + self.name


class Borrowing(models.Model):
    isbn = models.ForeignKey(Book, on_delete=models.CASCADE)
    rid = models.ForeignKey(Reader, on_delete=models.CASCADE)
    rent_date = models.DateTimeField()
    return_date =models.DateTimeField()
    def __str__(self):
        return "book {} borrowed by {} at {} to {}".format(self.isbn, self.rid, self.rent_date, self.return_date)
