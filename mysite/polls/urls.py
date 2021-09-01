from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<specifics/int:question_id>/', views.detail, naem='detail'),
    path('<int:question_id>/', views.result, name='result'),
    path('<int:question_id>/', views.vote, name='vote'),
]