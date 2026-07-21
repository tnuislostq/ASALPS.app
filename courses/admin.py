from django.contrib import admin

# Register your models here.
from .models import Course, LearningTask

admin.site.register(Course)
admin.site.register(LearningTask)