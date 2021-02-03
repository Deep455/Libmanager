from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from libmanager.models import Books_collection, requested_books, Student_Detail
from django.contrib import messages



# Create your views here.
def homepage(request):
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request, 'homepage.html')


def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('user_name')
        password = request.POST.get('user_pass')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")

        else:
            return render(request, 'loginuser.html')

    return render(request, 'loginuser.html')


def logoutuser(request):
    logout(request)
    return render(request, 'logoutuser.html')


def addbook(request):
    if request.user.is_anonymous:
        return redirect("/login")

    if request.method == "POST":
        book_id = request.POST.get('book_id')
        book_name = request.POST.get('book_name')
        author = request.POST.get('author')
        published_year = request.POST.get('published_year')
        category = request.POST.get('category')
        language = request.POST.get('language')

        book_info_collect = Books_collection(book_id=book_id, book_name=book_name, author=author,
                                             published_year=published_year, category=category, language=language)

        book_info_collect.save()
        messages.success(request, 'submission successful')

    return render(request, 'addbook.html')


def requestbook(request):
    if request.user.is_anonymous:
        return redirect("/login")

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        req = request.POST.get('request')
        roll_number = request.POST.get('roll_number')

        request_info = requested_books(name=name, roll_number=roll_number, email=email, requests=req)

        request_info.save()

    return render(request, 'requestbook.html')


def about(request):
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request, 'about.html')


def contact(request):
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request, 'contact.html')


def addstudent(request):
    if request.user.is_anonymous:
        return redirect("/login")

    if request.method == "POST":
        student_name = request.POST.get('student_name')
        roll_number = request.POST.get('roll_number')
        branch = request.POST.get('branch')
        year = request.POST.get('year')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        if len(email) < 4:
            messages.error(request, "Please fill the form correctly")
        else:
            details = Student_Detail(student_name=student_name, roll_number=roll_number, branch=branch, year=year,
                                 gender=gender, email=email)
            details.save()
            messages.success(request, 'Registration Successful')


    return render(request, 'addstudent.html')


def studentinfo(request):
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request, 'studentinfo.html')


def borrowbook(request):
    if request.user.is_anonymous:
        return redirect("/login")

    if request.method == "POST":
        roll_no = request.POST.get('roll_no')
        asked_book = request.POST.get('asked_book')

        if Student_Detail.objects.filter(roll_number=roll_no).exists() and Books_collection.objects.filter(
                book_id=asked_book).exists():

            Books_collection.objects.filter(book_id=asked_book).update(availibility=False)
            Books_collection.objects.filter(book_id=asked_book).update(borrowed_by=roll_no)
            messages.success(request, 'Records Updated,Student may borrow the book now')
            #  here add submitted

        else:
            messages.error(request,'No such record found, check the roll number or book id')  # here add not submitted

    return render(request, 'borrowbook.html')


def returnbook(request):
    if request.user.is_anonymous:
        return redirect("/login")

    if request.method == "POST":
        roll_no = request.POST.get('roll_no')
        return_book = request.POST.get('return_book')

        if Books_collection.objects.filter(book_id=return_book).filter(borrowed_by=roll_no).exists():
            Books_collection.objects.filter(book_id=return_book).update(availibility=True)
            Books_collection.objects.filter(book_id=return_book).update(borrowed_by=0)
            messages.success(request, 'Records Updated,Student may return the book now')

            # here add submitted


        else:
            messages.error(request, 'No such record found, check the roll number or book id')


    return render(request, 'returnbook.html')

