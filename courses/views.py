from django.shortcuts import render

# Create your views here.
from .models import Course

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})
from django.shortcuts import redirect, get_object_or_404
from .models import LearningTask

def toggle_task(request, task_id):
    task = get_object_or_404(LearningTask, id=task_id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('dashboard_index')