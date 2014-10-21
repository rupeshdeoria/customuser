from django.db import models

# Create your models here.
class  Book(models.Model):
    book_name = models.CharField(max_length=10)
    book_title = models.CharField(max_length=40)
