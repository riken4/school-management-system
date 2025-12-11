from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('staff', 'Staff'),
    )
    name = models.CharField(max_length=255, blank=True)
    roll_number = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255)
    enrollment_date = models.DateField(auto_now_add=True)     
    # class_name = models.ForeignKey(School_Class, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='user_image/', blank=True, null=True)

    @property
    def is_admin(self):
        return self.user_type == 'admin'
    
    @property
    def is_teacher(self):
        return self.user_type == 'teacher'
    
    @property
    def is_student(self):
        return self.user_type == 'student'
    
    @property
    def is_staff_member(self):
        return self.user_type == 'staff'
    
    def __str__(self):
        return self.name

                
class School_Class(models.Model):
    class_name = models.CharField(max_length=50) 
    section = models.CharField(max_length=10, blank=True)
    teacher = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    student = models.ManyToManyField(CustomUser, related_name='classes', blank=True)

    def __str__(self):
        return self.class_name


class worker(models.Model):
    name = models.CharField(max_length=50)


class herosection(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    student_class = models.CharField(max_length=50)
    section = models.CharField(max_length=10)
    image = models.ImageField(upload_to='user_image/', blank=True, null=True)

    def __str__(self):
        return self.name

class Teacher(CustomUser):
    subject = models.CharField(max_length=100)


    def __str__(self):
        return self.name