from django.contrib import admin
from shanuapp1.models import Student

from .models import User
from .models import Student1
from .models import Student2,Teacher,Contractor

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=('id','stuid','stuname','stuemail','stupass')

admin.site.register(Student,StudentAdmin)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','email','password')

@admin.register(Student1)
class Student1Admin(admin.ModelAdmin):
    list_display=['id','name','roll','city','marks','pass_date']

@admin.register(Student2)
class Student2Admin(admin.ModelAdmin):
    list_display=['id','name','age','fees']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=['id','name','age','date','salary']

@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display=['id','name','age','date','payment']
    
