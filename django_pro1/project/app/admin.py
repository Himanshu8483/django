from django.contrib import admin
from .models import Book, Students

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'stuname', 'stuemail', 'stuphone', 'stuedu', 'stugender')
    search_fields = ('stuname', 'stuemail', 'stuedu')
    list_filter = ('stuname', 'stuedu' )  # Filter by name and education

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_title', 'student_name', 'clas', 'section', 'issue_date', 'price')
    search_fields = ('book_title', 'student_name')
    list_filter = ('clas', 'section')  # Filter by class and section
