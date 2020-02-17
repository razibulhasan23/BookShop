from django.db import models


class ReferBook(models.Model):
    isbn = models.IntegerField(null=False)
    title = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "refer_books"


class ReferPages(models.Model):
    isbn = models.IntegerField(null=False)
    content = models.FileField(null=False)
    cover = models.FileField(null=False)
    refer_book = models.ForeignKey(ReferBook, on_delete=models.CASCADE, related_name='refer_books')

    def __str__(self):
        return self.refer_book.title

    class Meta:
        db_table = "refer_pages"
