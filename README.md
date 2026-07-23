# ASALPS - Adaptive Skill Audit & Learning Path System

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![Render](https://img.shields.io/badge/Render-Deployed-46E3B7?style=for-the-badge&logo=render&logoColor=white)

**ASALPS** is a full-stack web application built with Python and Django designed to help users track structured skill learning paths, perform interactive skill audits, and monitor course completion metrics in real time.

---

## 🌐 Live Demo

* **Live Application:** [https://asalps-app.onrender.com](https://asalps-app.onrender.com)
* **GitHub Repository:** [https://github.com/tnuislostq/ASALPS.app](https://github.com/tnuislostq/ASALPS.app)

---

## ✨ Features

* 📚 **Course Catalog:** Browse available structured learning paths across categories like Web Development, Cloud Engineering, and Data Structures.
* 📊 **Interactive Skill Audit:** Dynamically toggle task completion and track progress percentages in real time.
* 📈 **Analytics Dashboard:** Visual representation of enrolled courses, total tasks, completed milestones, and overall completion progress.
* ⚡ **Automated Data Seeding:** Custom Django management commands automatically seed course data upon deployment.
* 🚀 **Production-Ready Deployment:** Hosted on Render using Gunicorn WSGI server and WhiteNoise static asset management.

---

## 🛠️ Tech Stack

* **Backend:** Python 3, Django 6
* **Frontend:** HTML5, CSS3, Bootstrap 5, Django Template Language (DTL)
* **Database:** SQLite3 (Development & Production Seeding)
* **Static Assets:** WhiteNoise
* **Production Server:** Gunicorn
* **Deployment & CI/CD:** Render, GitHub Actions / Auto-Deploy

---

## 📁 Project Structure

```text
ASALPS/
├── asalps_core/        # Project settings, URL routing, WSGI configuration
├── courses/            # App for courses, tasks, and seed_data management commands
├── dashboard/          # App for learning analytics and progress calculations
├── staticfiles/        # Compiled static assets served by WhiteNoise
├── manage.py           # Django CLI utility
├── requirements.txt    # Python dependencies
<<<<<<< HEAD
└── README.md           # Project documentation
=======
└── README.md           # Project documentation
>>>>>>> e1bd114 (Expand dataset to 8 skill paths with 34% baseline progress audit)
