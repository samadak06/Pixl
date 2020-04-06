from django.shortcuts import render
from .models import Photo
from django.views.generic import (
    ListView,
)

class PhotoListView(ListView):
    model = Photo
    template_name = 'gallery/home.html'
    context_object_name = 'photos'
    ordering = ['-date_posted']
