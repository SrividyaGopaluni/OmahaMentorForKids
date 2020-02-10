from django.db import models
from django.utils import timezone

# Create your models here.

class Mentor(models.Model):
    mentor_ID = models.CharField(max_length=50)
    mentor_LastName = models.CharField(max_length=100)
    mentor_FirstName = models.CharField(max_length=100)
    mentor_email = models.EmailField(max_length=100)
    mentor_address = models.CharField(max_length=200)
    mentor_city = models.CharField(max_length=50)
    mentor_state = models.CharField(max_length=50)
    mentor_zipcode = models.CharField(max_length=10)
    mentor_phone_number = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.mentor_LastName)


class Student(models.Model):
    student_ID = models.CharField(max_length=50)
    student_schoolID = models.CharField(max_length=100, blank=True)
    student_FirstName = models.CharField(max_length=100)
    student_LastName = models.CharField(max_length=100)
    student_gender = models.CharField(max_length=100)
    student_dateofbirth = models.DateTimeField(max_length=50)
    student_email = models.EmailField(max_length=100)
    student_address = models.CharField(max_length=200)
    student_city = models.CharField(max_length=50)
    student_state = models.CharField(max_length=50)
    student_zipcode = models.CharField(max_length=10)
    student_phone_number = models.CharField(max_length=50)
    student_school = models.CharField(max_length=50)
    student_notes =models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.student_FirstName)

class StudentMentor(models.Model):

    group_ID = models.CharField(max_length=50)
    group_Name= models.CharField(max_length=50)
    student_ID = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student')
    mentor_ID = models.ForeignKey(Mentor,on_delete=models.CASCADE, related_name='student')

    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.group_Name)