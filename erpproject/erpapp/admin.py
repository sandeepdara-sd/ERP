from django.contrib import admin

from .models import Admin, Department,  Student, Faculty, Course

admin.site.register(Admin)
admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Course)