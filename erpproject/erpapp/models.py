from django.db import models

class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50,unique=True,blank=False)
    password = models.CharField(max_length=50,blank=False)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "admin_table"

class Department(models.Model):
    id=models.PositiveIntegerField(primary_key=True,verbose_name="Department Id")
    name=models.CharField(max_length=100,blank=False,unique=True,verbose_name="Department Name")
    location = models.CharField(max_length=100, blank=False,verbose_name="Department Location")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "department_table"

class Faculty(models.Model):
    id=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=100,blank=False)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    email=models.EmailField(max_length=50,blank=False,unique=True)
    username=models.CharField(max_length=50,blank=False,unique=True)
    password = models.CharField(max_length=50, blank=False)
    registrationtime = models.DateTimeField(blank=False,auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "faculty_table"


class Course(models.Model):
    id=models.AutoField(primary_key=True)
    category_choices = (("Core Courses", "Core Courses"), ("Elective Courses", "Elective Courses"), ("General Education Courses", "General Education Courses"), ("Practicals and Labs","Practicals and Labs"),("Seminar and Workshops","Seminar and Workshops"))
    category = models.CharField(max_length=100, blank=False,choices=category_choices)
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=200,blank=False)
    price = models.PositiveIntegerField(blank=False)
    image = models.FileField(blank=False,upload_to="productimages")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "course_table"

class Student(models.Model):
    id=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=100,blank=False)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    email=models.EmailField(max_length=50,blank=False,unique=True)
    username=models.CharField(max_length=50,blank=False,unique=True)
    password = models.CharField(max_length=50, blank=False)
    registrationtime = models.DateTimeField(blank=False,auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "student_table"


