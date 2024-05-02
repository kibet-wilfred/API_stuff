from django.contrib import admin
from django.urls import path
from app import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('profiles/',views.profiles)

]
urlpatterns = format_suffix_patterns(urlpatterns)