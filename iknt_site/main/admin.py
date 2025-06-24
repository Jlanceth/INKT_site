from django.contrib import admin
from .models import News, Teacher

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    list_filter = ('published_date',)
    search_fields = ('title', 'content')
    date_hierarchy = 'published_date'
    ordering = ('-published_date',)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'position', 'department')
    list_filter = ('position', 'department')
    search_fields = ('last_name', 'first_name', 'middle_name', 'department')
    ordering = ('last_name', 'first_name')

admin.site.register(News, NewsAdmin)
admin.site.register(Teacher, TeacherAdmin)