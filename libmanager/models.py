from django.db import models

# Create your models here.
class Books_collection(models.Model):
    book_id=models.IntegerField(unique=True)
    book_name=models.CharField(max_length=120)
    author=models.CharField(max_length=120)
    published_year=models.IntegerField()
    category=models.CharField(max_length=120)
    language=models.CharField(max_length=120)

    def __str__(self):
        return self.book_name
    
class requested_books(models.Model):
    name=models.CharField(max_length=120)
    email=models.EmailField()
    requests=models.TextField()

    def __str__(self):
        return self.name
    