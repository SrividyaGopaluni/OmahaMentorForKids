from django.contrib import admin
from .models import Mentor,Student,StudentMentor

# Register your models here.

class MentorList(admin.ModelAdmin):
    list_display = ( 'mentor_LastName', 'mentor_email', 'mentor_phone_number' )
    list_filter = ( 'mentor_LastName', 'mentor_email')
    search_fields = ('mentor_LastName', )
    ordering = ['mentor_LastName']

class StudentList(admin.ModelAdmin):
    list_display = ( 'student_LastName', 'student_email', 'student_phone_number' )
    list_filter = ( 'student_LastName', 'student_email')
    search_fields = ('student_LastName', )
    ordering = ['student_LastName']

class StudentMentorList(admin.ModelAdmin):
    list_display = ( 'group_Name',)
    list_filter = ( 'group_Name', )
    search_fields = ('group_Name', )
    ordering = ['group_Name']




admin.site.register(Mentor,MentorList)
admin.site.register(Student,StudentList)
admin.site.register(StudentMentor,StudentMentorList)



