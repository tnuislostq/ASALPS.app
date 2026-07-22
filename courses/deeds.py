from courses.models import Course, LearningTask

def seed_database():
    if Course.objects.exists():
        return  # Don't duplicate if data already exists

    courses_data = [
        {
            "title": "Full-Stack Web Development",
            "category": "Web Dev",
            "description": "Master Python, Django, React, and REST APIs to build production-ready applications.",
            "tasks": [
                "Understand Django MVT Architecture",
                "Design Database Schemas with Models",
                "Build RESTful APIs with Django REST Framework",
                "Deploy Application to Render"
            ]
        },
        {
            "title": "AWS & Cloud Development",
            "category": "Cloud & DevOps",
            "description": "Learn cloud infrastructure, EC2, S3, IAM, and automated CI/CD deployment pipelines.",
            "tasks": [
                "Configure AWS IAM Roles & Policies",
                "Deploy Web Server on EC2",
                "Set Up S3 Bucket for Static Assets",
                "Build CI/CD Pipeline with GitHub Actions"
            ]
        },
        {
            "title": "Data Structures & Algorithms",
            "category": "Computer Science",
            "description": "Strengthen problem-solving skills with core data structures, algorithms, and time complexity optimization.",
            "tasks": [
                "Master Arrays & Hash Maps",
                "Implement Linked Lists & Trees",
                "Analyze Time Complexity (Big-O)",
                "Solve Dynamic Programming Problems"
            ]
        }
    ]

    for item in courses_data:
        course = Course.objects.create(
            title=item["title"],
            category=item["category"],
            description=item["description"]
        )
        for task_title in item["tasks"]:
            LearningTask.objects.create(
                course=course,
                title=task_title,
                is_completed=False
            )