from django.urls import path

from . import views

urlpatterns = [
    path('articles/<int:year>/', views.year_archive)
]
