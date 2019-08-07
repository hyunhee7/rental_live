from django.urls import path
from blog.views import *
urlpatterns = [
    path("", index, name="index"),
    path("person/",person, name="person"),
    path("list/",list, name="list"),
    path("recommand/",recommand, name="recommand"),
]