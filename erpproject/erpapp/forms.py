from django import forms

from .models import Admin,  Department, Student, Faculty, Course


class DateInput(forms.DateInput):
    input_type = "date"

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"

class UpdateDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"

class ProductForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        labels = {"category":"Select Category"}

class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"
        widgets = {"password":forms.PasswordInput()}

class EmployeeRegistrationForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = "__all__"
        widgets = {"dateofbirth":DateInput(),"password":forms.PasswordInput(),'fullname': forms.TextInput(attrs={'placeholder': 'Enter Full Name'}),'email': forms.TextInput(attrs={'placeholder': 'Enter Email Address'})}

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {"dateofbirth":DateInput(),"password":forms.PasswordInput(),'fullname': forms.TextInput(attrs={'placeholder': 'Enter Full Name'}),'email': forms.TextInput(attrs={'placeholder': 'Enter Email Address'})}
