from django.shortcuts import render
from .models import Student, Discount, Book, FormattedBook, RecentBook

def homepage(request):
    student = Student.objects.last()
    discount = Discount.objects.last()
    book = Book.objects.last()

    formatted_book = FormattedBook.objects.get(id=book.id) if book else None
    recent_book = RecentBook.objects.get(id=book.id) if book else None

    context = {
        'student': student,
        'student_age': student.calculate_age() if student else None,

        'discount': discount,
        'is_discount_active': discount.is_eligible() if discount else None,

        'book': book,
        'formatted_details': formatted_book.formatted_details() if formatted_book else None,
        'is_recent': recent_book.is_recent() if recent_book else None,
    }

    return render(request, 'homepage.html', context)


from django.shortcuts import render
from .models import Student, Teacher, Discount, Promotion

def dashboard(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    discounts = Discount.objects.all()
    promotions = Promotion.objects.all()

    # Prepare data with age and eligibility
    student_data = [
        {"name": student.name, "age": student.calculate_age()}
        for student in students
    ]
    teacher_data = [
        {"name": teacher.name, "age": teacher.calculate_age()}
        for teacher in teachers
    ]
    discount_data = [
        {"name": discount.name, "percentage": discount.percentage, "active": discount.is_eligible()}
        for discount in discounts
    ]
    promotion_data = [
        {"title": promo.title, "description": promo.description, "active": promo.is_eligible()}
        for promo in promotions
    ]

    return render(request, "dashboard.html", {
        "students": student_data,
        "teachers": teacher_data,
        "discounts": discount_data,
        "promotions": promotion_data
    })

