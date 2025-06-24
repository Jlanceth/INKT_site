from django.shortcuts import render
from .models import News, Teacher


def home(request):
    latest_news = News.objects.all()[:5]
    return render(request, 'pages/home.html', {'latest_news': latest_news})


def news(request):
    news_list = News.objects.all().order_by('-published_date')
    return render(request, 'pages/news.html', {'news_list': news_list})


def news_detail(request, pk):
    news_item = News.objects.get(pk=pk)
    return render(request, 'pages/news_detail.html', {'news_item': news_item})


def about(request):
    return render(request, 'pages/about.html')


def teachers(request):
    teachers_list = Teacher.objects.all().order_by('last_name')
    return render(request, 'pages/teachers.html', {'teachers_list': teachers_list})


def teacher_detail(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    return render(request, 'pages/teacher_detail.html', {'teacher': teacher})


def contacts(request):
    return render(request, 'pages/contacts.html')