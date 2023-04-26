from django.urls import re_path
from calc import views

urlpatterns = [
    re_path('', views.index, name='index'),
]
