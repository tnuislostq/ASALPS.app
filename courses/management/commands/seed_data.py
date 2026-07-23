from django.core.management.base import BaseCommand
from courses.models import Course, LearningTask

class Command(BaseCommand):
    help = 'Seeds 8 realistic learning paths with pre-completed tasks for a live audit dashboard'

    def handle(self, *args, **kwargs):
        # Clear existing data to ensure a fresh, accurate 8-path seed
        LearningTask.objects.all().delete()
        Course.objects.all().delete()

        seed_paths = [
            {
                "title": "Full-Stack Web Development",
                "category": "Web Dev",
                "description": "Master modern web architectures with Python, Django, REST APIs, and responsive frontend design.",
                "tasks": [
                    ("Understand Django MVT & Routing Architecture", True),
                    ("Design Relational Database Schemas with Models", True),
                    ("Build RESTful APIs with Django REST Framework", False),
                    ("Deploy Application to Production via Render & Gunicorn", True),
                ]
            },
            {
                "title": "AWS Cloud Engineering",
                "category": "Cloud & DevOps",
                "description": "Architect scalable cloud systems using AWS core services, infrastructure as code, and CI/CD pipelines.",
                "tasks": [
                    ("Configure AWS IAM Roles & Least-Privilege Policies", True),
                    ("Deploy & Configure EC2 Instances with Nginx", True),
                    ("Set Up S3 Storage Buckets & Static Hosting", False),
                    ("Automate Deployments with GitHub Actions CI/CD", False),
                ]
            },
            {
                "title": "Data Structures & Algorithms",
                "category": "Computer Science",
                "description": "Strengthen algorithmic problem-solving, memory analysis, and core data structure implementations.",
                "tasks": [
                    ("Master Array Manipulations & Two-Pointer Patterns", True),
                    ("Implement Singly & Doubly Linked Lists", True),
                    ("Analyze Time & Space Complexity (Big-O Notation)", True),
                    ("Solve Dynamic Programming & Graph Traversal Problems", False),
                ]
            },
            {
                "title": "Data Science & Analytics",
                "category": "Data Science",
                "description": "Perform end-to-end data processing, exploratory analysis, and statistical visualization using Python.",
                "tasks": [
                    ("Clean & Transform Raw Datasets with Pandas", True),
                    ("Create Interactive Visualizations using Seaborn & Matplotlib", False),
                    ("Perform Exploratory Data Analysis (EDA) on Business Datasets", False),
                    ("Build Predictive Models using Scikit-Learn", False),
                ]
            },
            {
                "title": "Applied AI & Machine Learning",
                "category": "AI & ML",
                "description": "Explore supervised machine learning algorithms, deep learning models, and NLP workflows.",
                "tasks": [
                    ("Implement Supervised Learning (Regression & Classification)", True),
                    ("Evaluate Models with Precision, Recall, and F1-Score", False),
                    ("Fine-tune Pre-trained Transformers for Natural Language Tasks", False),
                    ("Deploy ML Models via FastAPI Endpoints", False),
                ]
            },
            {
                "title": "Database Engineering & SQL",
                "category": "Databases",
                "description": "Master relational database design, complex SQL queries, index optimization, and ACID compliance.",
                "tasks": [
                    ("Write Complex JOINs, Aggregations, and Subqueries", True),
                    ("Design Normalized Schemas (1NF, 2NF, 3NF)", True),
                    ("Optimize Query Performance using B-Tree Indexing", False),
                    ("Manage Database Transactions & Lock Strategies", False),
                ]
            },
            {
                "title": "Cross-Platform Mobile Development",
                "category": "Mobile Dev",
                "description": "Build high-performance mobile applications across iOS and Android platforms.",
                "tasks": [
                    ("Set Up Cross-Platform Navigation & Component Architecture", False),
                    ("Integrate REST API Endpoints with Async State Management", False),
                    ("Implement Native Device Permissions & Push Notifications", False),
                    ("Build Production Binaries for App Store Release", False),
                ]
            },
            {
                "title": "Cybersecurity & Web Application Defense",
                "category": "Security",
                "description": "Understand security principles, vulnerability assessment, web exploits, and defensive coding.",
                "tasks": [
                    ("Identify OWASP Top 10 Vulnerabilities (XSS, SQLi, CSRF)", True),
                    ("Implement Secure User Authentication & JWT Auth", True),
                    ("Configure HTTPS/TLS Certificates & Security Headers", False),
                    ("Conduct Static & Dynamic Application Security Testing", False),
                ]
            }
        ]

        for path in seed_paths:
            course = Course.objects.create(
                title=path["title"],
                category=path["category"],
                description=path["description"]
            )
            for title, is_completed in path["tasks"]:
                LearningTask.objects.create(
                    course=course,
                    title=title,
                    is_completed=is_completed
                )

        self.stdout.write(self.style.SUCCESS("Successfully seeded 8 learning paths with 34% completion rate!"))