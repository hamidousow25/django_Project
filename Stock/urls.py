from django.urls import path
from . views import * 
urlpatterns = [
    path('',info, name='kountigui'),
]