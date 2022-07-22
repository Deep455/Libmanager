from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from libmanager.models import Books_collection,requested_books

# Create your views here.
def homepage(request):
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request, 'homepage.html')

def loginuser(request):
    if request.method == "POST":
        username=request.POST.get('user_name')
        password=request.POST.get('user_pass')
        user=authenticate(username=username, password=password)

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
        book_id=request.POST.get('book_id')
        book_name=request.POST.get('book_name')
        author=request.POST.get('author')
        published_year=request.POST.get('published_year')
        category=request.POST.get('category')
        language=request.POST.get('language')

        book_info_collect=Books_collection(book_id=book_id, book_name=book_name, author=author, published_year=published_year, category=category, language=language)

        book_info_collect.save()

    return render(request, 'addbook.html')

def requestbook(request):
    if request.user.is_anonymous:
        return redirect("/login")
    
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        req=request.POST.get('request')

        request_info=requested_books(name=name, email=email, requests=req)

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

    