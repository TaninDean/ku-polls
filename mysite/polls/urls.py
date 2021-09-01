from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.DetailView.as_view, naem='detail'),
    path('<int:pk>/results/', views.result, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]