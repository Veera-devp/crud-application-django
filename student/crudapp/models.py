from django.db import models


# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=10, unique=True)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_phone = models.CharField(max_length=15)

    def __str__(self):
        return self.student_name
