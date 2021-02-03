from django.db import models


# Create your models here.
class Books_collection(models.Model):
    book_id = models.IntegerField(unique=True)
    book_name = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    published_year = models.IntegerField()
    category = models.CharField(max_length=120)
    language = models.CharField(max_length=120)
    borrowed_by = models.IntegerField(default=0)
    availibility = models.BooleanField(default=True)

    def __str__(self):
        return self.book_name


class requested_books(models.Model):
    name = models.CharField(max_length=120)
    roll_number = models.IntegerField(default=0)#change this later
    email = models.EmailField()
    requests = models.TextField()

    def __str__(self):
        return self.name + "-" + str(self.roll_number)


class Student_Detail(models.Model):
    student_name = models.CharField(max_length=120)
    roll_number = models.IntegerField(unique=True)
    BRANCHES_NAME = [('Ceramic Engineering', 'Ceramic Engineering'), ('Chemical Engineering', 'Chemical Engineering'),
                     ('Civil Engineering', 'Civil Engineering'),
                     ('Computer Science and Engineering', 'Computer Science and Engineering'),
                     ('Electrical Engineering', 'Electrical Engineering'),
                     ('Electronics Engineering', 'Electronics Engineering'),
                     ('Mechanical Engineering', 'Mechanical Engineering'),
                     ('Metallurgical Engineering', 'Metallurgical Engineering'),
                     ('Mining Engineering', 'Mining Engineering'),
                     ('Pharmaceutical Engineering', 'Pharmaceutical Engineering')]
    branch = models.CharField(max_length=120, choices=BRANCHES_NAME)
    YEARS = [('1st', '1st Year'), ('2nd', '2nd Year'), ('3rd', '3rd Year'), ('4th', '4th Year'), ('5th', '5th Year')]
    year = models.CharField(max_length=10, choices=YEARS)
    GENDER = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    gender = models.CharField(max_length=10, choices=GENDER)
    email = models.EmailField()

    def __str__(self):
        return str(self.roll_number) + "-" + self.student_name
