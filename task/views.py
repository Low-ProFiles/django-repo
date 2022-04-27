from django.shortcuts import render


def index(request):
    return render(request, "task/index.html")


def pokeball(request):
    return render(request, "task/pokeball.html")


def lorem(request):
    return render(request, "task/lorem.html")



