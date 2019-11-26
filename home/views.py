from django.shortcuts import render, redirect


def home(request):
    return render(request, 'base.html')


def add(request):
    return render(request, 'add.html')


def clear(request):
    return render(request, 'clear.html')
