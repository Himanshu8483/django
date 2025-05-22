# from django.contrib import admin
# from .models import Student, Teacher, Discount, Promotion, Book

# # Registering all concrete (non-abstract) models
# admin.site.register(Student)
# admin.site.register(Teacher)
# admin.site.register(Discount)
# admin.site.register(Promotion)
# admin.site.register(Book)



# from datetime import date
# from yourapp.models import Student, Teacher, Discount, Promotion

# # Create some students and teachers
# student1 = Student.objects.create(name="Himanshu", birth_date=date(2000, 5, 15))
# teacher1 = Teacher.objects.create(name="Mr. Neeraj", birth_date=date(1980, 10, 30))

# # Calculate ages
# print(student1.name, "age:", student1.calculate_age())  # Himanshu age
# print(teacher1.name, "age:", teacher1.calculate_age())  # Mr. Neeraj age

# # Create discount and promotion offers
# discount1 = Discount.objects.create(
#     name="Summer Sale", 
#     percentage=20.0, 
#     start_date=date(2025, 5, 1), 
#     end_date=date(2025, 5, 31)
# )

# promotion1 = Promotion.objects.create(
#     title="Holiday Special", 
#     description="Buy one get one free", 
#     start_date=date(2025, 12, 15), 
#     end_date=date(2026, 1, 5)
# )

# # Check eligibility
# print(discount1.name, "is eligible today?", discount1.is_eligible())
# print(promotion1.title, "is eligible today?", promotion1.is_eligible())








# from datetime import date
# from yourapp.models import Book, OrderedBook, FormattedBook, RecentBook

# # Create some books
# book1 = Book.objects.create(title="Python Basics", published_date=date(2024, 6, 15))
# book2 = Book.objects.create(title="Advanced Django", published_date=date(2023, 8, 10))
# book3 = Book.objects.create(title="AI Revolution", published_date=date(2022, 11, 20))

# # Query using proxy model OrderedBook (should order by published_date descending)
# for b in OrderedBook.objects.all():
#     print(b.title, b.published_date)

# # Use FormattedBook's custom method
# fb = FormattedBook.objects.get(id=book1.id)
# print(fb.formatted_details())

# # Check recent books (published this year or last year)
# for b in RecentBook.objects.all():
#     print(b.title, "is recent?", b.is_recent())

from django.contrib import admin
from .models import Student, Teacher

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'get_age')

    def get_age(self, obj):
        return obj.calculate_age()
    get_age.short_description = 'Age'


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'get_age')

    def get_age(self, obj):
        return obj.calculate_age()
    get_age.short_description = 'Age'


from .models import Discount, Promotion

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'percentage', 'is_currently_active')

    def is_currently_active(self, obj):
        return obj.is_eligible()
    is_currently_active.boolean = True  # Shows a green tick / red X
    is_currently_active.short_description = 'Is Active'


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'description', 'is_currently_active')

    def is_currently_active(self, obj):
        return obj.is_eligible()
    is_currently_active.boolean = True
    is_currently_active.short_description = 'Is Active'


from .models import Book, OrderedBook, FormattedBook, RecentBook

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')

@admin.register(FormattedBook)
class FormattedBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'formatted_info')

    def formatted_info(self, obj):
        return obj.formatted_details()
    formatted_info.short_description = 'Formatted Details'

@admin.register(RecentBook)
class RecentBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'is_recent_book')

    def is_recent_book(self, obj):
        return obj.is_recent()
    is_recent_book.boolean = True
    is_recent_book.short_description = 'Recent?'

@admin.register(OrderedBook)
class OrderedBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
