from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('about/', views.about, name='about'),
    path('teachers/', views.teachers, name='teachers'),
    path('teachers/<int:pk>/', views.teacher_detail, name='teacher_detail'),
    path('contacts/', views.contacts, name='contacts'),
]