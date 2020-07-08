from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
import os
import shutil
from os import path
from .forms import BookForm
from .models import Book


class Home(TemplateView):
    template_name = 'home.html'


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        file_path = os.path.join('./media', 'input.txt') # full path to text.
        data_file = open(file_path , 'rb')   #I used'rb' here since I got an 'gbk' decode error
        data = data_file.read()
        file1 = open(file_path,"r+")
        print ("Output of Read function is ")
        print (file1.read())
        print
        print("data=", data)
    return render(request, 'upload.html', context)

def fun1(request):
    context = {}
    if request.method == 'POST':
        shutil.copyfile('./media/input.txt', './media/fun1.txt')
        fs = FileSystemStorage()
        context['url'] = fs.url('./fun1.txt')
        file_path = os.path.join('./media','fun1.txt') # full path to text.
        data_file = open(file_path , 'rb')   #I used'rb' here since I got an 'gbk' decode error
        data = data_file.read()
        file1 = open(file_path,"r+")
        print ("Output of Read function is ")
        print (file1.read())
        print
        print("data=", data)
    return render(request, 'fun1.html', context)


def fun2(request):
    context = {}
    if request.method == 'POST':
        shutil.copyfile('./media/input.txt', './media/fun2.txt')
        fs = FileSystemStorage()
        context['url'] = fs.url('./fun2.txt')
        file_path = os.path.join('./media','fun2.txt') # full path to text.
        '''Your Code Will Come Here data_file = open(file_path , 'rb')   #I used'rb' here since I got an 'gbk' decode error
        data = data_file.read()
        file1 = open(file_path,"r+")
        print ("Output of Read function is ")
        print (file1.read())
        print
        print("data=", data)'''
    return render(request, 'fun2.html', context)

def fun3(request):
    context = {}
    if request.method == 'POST':
        shutil.copyfile('./media/input.txt', './media/fun3.txt')
        fs = FileSystemStorage()
        context['url'] = fs.url('./fun3.txt')
        file_path = os.path.join('./media','fun3.txt') # full path to text.
        '''data_file = open(file_path , 'rb')   #I used'rb' here since I got an 'gbk' decode error
        data = data_file.read()
        file1 = open(file_path,"r+")
        print ("Output of Read function is ")
        print (file1.read())
        print
        print("data=", data)'''
    return render(request, 'fun3.html', context)

def fun4(request):
    context = {}
    if request.method == 'POST':
        shutil.copyfile('./media/input.txt', './media/fun4.txt')
        fs = FileSystemStorage()
        context['url'] = fs.url('./fun4.txt')
        file_path = os.path.join('./media','fun4.txt') # full path to text.
        #data_file = open(file_path , 'rb')   #I used'rb' here since I got an 'gbk' decode error
        #data = data_file.read()
        #file1 = open(file_path,"r+")
        #print ("Output of Read function is ")
        #print (file1.read())
        #print
        #print("data=", data)
    return render(request, 'fun4.html', context)

def fun5(request):
    context = {}
    if request.method == 'POST':
        shutil.copyfile('./media/input.txt', './media/fun5.txt')
        fs = FileSystemStorage()
        context['url'] = fs.url('./fun5.txt')
        file_path = os.path.join('./media','fun5.txt') # full path to text.
        '''data_file = open(file_path , 'rb')   #I used'rb' here since I got an 'gbk' decode error
        data = data_file.read()
        file1 = open(file_path,"r+")
        print ("Output of Read function is ")
        print (file1.read())
        print
        print("data=", data)'''
    return render(request, 'fun5.html', context)

def fun6(request):
    context = {}
    if request.method == 'POST':
        shutil.copyfile('./media/input.txt', './media/fun6.txt')
        fs = FileSystemStorage()
        context['url'] = fs.url('./fun6.txt')
        file_path = os.path.join('./media','fun6.txt') # full path to text.
        '''data_file = open(file_path , 'rb')   #I used'rb' here since I got an 'gbk' decode error
        data = data_file.read()
        file1 = open(file_path,"r+")
        print ("Output of Read function is ")
        print (file1.read())
        print
        print("data=", data)'''
    return render(request, 'fun6.html', context)

def fun7(request):
    context = {}
    if request.method == 'POST':
        shutil.copyfile('./media/input.txt', './media/fun7.txt')
        fs = FileSystemStorage()
        context['url'] = fs.url('./fun7.txt')
        file_path = os.path.join('./media','fun7.txt') # full path to text.
        '''data_file = open(file_path , 'rb')   #I used'rb' here since I got an 'gbk' decode error
        data = data_file.read()
        file1 = open(file_path,"r+")
        print ("Output of Read function is ")
        print (file1.read())
        print
        print("data=", data)'''
    return render(request, 'fun7.html', context)

def fun8(request):
    context = {}
    if request.method == 'POST':
        shutil.copyfile('./media/input.txt', './media/fun8.txt')
        fs = FileSystemStorage()
        context['url'] = fs.url('./fun8.txt')
        file_path = os.path.join('./media','fun8.txt') # full path to text.
        '''data_file = open(file_path , 'rb')   #I used'rb' here since I got an 'gbk' decode error
        data = data_file.read()
        file1 = open(file_path,"r+")
        print ("Output of Read function is ")
        print (file1.read())
        print
        print("data=", data)'''
    return render(request, 'fun8.html', context)
