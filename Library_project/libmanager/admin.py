from django.contrib import admin
# super user = admin and password = 1234
# Register your models here.
from libmanager.models import Books_collection, requested_books, Student_Detail

admin.site.register(Books_collection)
admin.site.register(requested_books)
admin.site.register(Student_Detail)