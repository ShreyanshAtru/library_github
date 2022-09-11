from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from books.models import Book
from books.serializers import BookSerializer
from .forms import BookForm, LoginForm, RegisterForm
from django.shortcuts import render 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response 


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'books/login.html'


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'books/register.html'
    success_url = reverse_lazy('login')


def view_books(request):
    books = Book.objects.all()
    return render(request, 'books/view_books.html', {'books':books})


def add_book(request):
    import pdb
    pdb.set_trace()
    form = BookForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'books/add_books.html', {'form':form})


@login_required
def delete_book(request, id):
    # import pdb
    # pdb.set_trace()
    book = Book.objects.get(pk=id)
    print(book)
    book.delete()
    return HttpResponse(f'this book is deleted of id : {{obj.id}}')


def update_books(request, id):
    book = get_object_or_404(Book, id=id)
    form = BookForm(request.POST or None, instance = book)
    print(book.book_title)
    return render(request, 'books/update_books.html', {'form':form})


@api_view(['POST'])
def bookcreate(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def bookupdate(request,pk):
    tasks = Book.objects.get(id=pk)
    serializer = BookSerializer(data=tasks,many=False)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def bookdelete(request,pk):
    tasks = Book.objects.get(id=pk)
    tasks.delete()
    return Response("Succesfully deleted!!")
