from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    image = models.ImageField(upload_to='news_images/', null=True, blank=True, verbose_name="Изображение")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-published_date']


class Teacher(models.Model):
    POSITION_CHOICES = [
        ('prof', 'Профессор'),
        ('docent', 'Доцент'),
        ('teacher', 'Преподаватель'),
        ('assistant', 'Ассистент'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    middle_name = models.CharField(max_length=100, verbose_name="Отчество", blank=True)
    position = models.CharField(max_length=50, choices=POSITION_CHOICES, verbose_name="Должность")
    department = models.CharField(max_length=200, verbose_name="Кафедра")
    bio = models.TextField(verbose_name="Биография", blank=True)
    photo = models.ImageField(upload_to='teachers_photos/', null=True, blank=True, verbose_name="Фото")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Телефон", blank=True)
    
    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"
    
    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"
        ordering = ['last_name', 'first_name']