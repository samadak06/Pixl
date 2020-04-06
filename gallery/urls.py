from . import views
from django.urls import path

urlpatterns = [
    path('', views.PhotoListView.as_view(), name='gallery-home')
]