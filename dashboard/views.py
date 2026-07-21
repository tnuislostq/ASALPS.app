from django.shortcuts import render

# Create your views here.
from courses.models import Course, LearningTask

def index(request):
    total_courses = Course.objects.count()
    total_tasks = LearningTask.objects.count()
    completed_tasks = LearningTask.objects.filter(is_completed=True).count()
    
    # Simple completion percentage calculation
    progress = 0
    if total_tasks > 0:
        progress = int((completed_tasks / total_tasks) * 100)

    context = {
        'total_courses': total_courses,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'progress': progress,
    }
    return render(request, 'dashboard/index.html', context)