from django.urls import path

from boots import views


urlpatterns = [
    path("home/", views.test_home),
    path("blog/", views.test_blog),
    path("contact/", views.test_contact),
    path("about/", views.test_about)
]
