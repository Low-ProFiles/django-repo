from django.shortcuts import render


def test_home(request):
    return render(request, "boots/index.html")


def test_blog(request):
    return render(request, "boots/blog.html")


def test_about(request):
    return render(request, "boots/about.html")


def test_contact(request):
    return render(request, "boots/contact.html")
