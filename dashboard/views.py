from django.shortcuts import render
from courses.models import Course, LearningTask

def index(request):
    total_courses = Course.objects.count()
    tasks = LearningTask.objects.all()
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(is_completed=True).count()
    
    progress = 0
    if total_tasks > 0:
        progress = int((completed_tasks / total_tasks) * 100)

    context = {
        'total_courses': total_courses,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'progress': progress,
        'tasks': tasks,
    }
    return render(request, 'dashboard/index.html', context)