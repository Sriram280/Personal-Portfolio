# Personal Portfolio Website

## Overview

A professional and responsive personal portfolio website developed using Python and Django. The website showcases my technical skills, education, projects, experience, resume, and contact information through a modern and interactive interface.

## Features

* Responsive portfolio design
* Professional profile section
* About Me section
* Technical skills with progress indicators
* Education details
* Experience section
* Project showcase
* GitHub and live project links
* Resume download
* Contact form
* Contact messages stored in the database
* Django Admin panel for managing portfolio content
* Dark/Light mode
* Animated typing effect
* Mobile-friendly design

## Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap 5
* Bootstrap Icons

### Backend

* Python
* Django

### Database

* SQLite

### Other Tools

* Git
* GitHub
* VS Code

## Project Structure

```text
django-portfolio/
│
├── main/
│   ├── migrations/
│   ├── templates/
│   │   └── main/
│   │       └── index.html
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── portfolio/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│       └── profile.jpeg
│
├── media/
├── manage.py
├── requirements.txt
└── README.md
```

## Database Models

The project uses Django models to manage portfolio information:

* **Skill** – Technical skills and proficiency
* **Project** – Personal and academic projects
* **Education** – Educational qualifications
* **Experience** – Work or internship experience
* **Contact** – Messages submitted through the contact form

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Sriram280/django-portfolio.git
```

### 2. Open the Project

```bash
cd django-portfolio
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Admin Account

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open the website:

```text
http://127.0.0.1:8000/
```

Admin panel:

```text
http://127.0.0.1:8000/admin/
```

## Admin Panel

The Django Admin panel allows portfolio content to be managed without modifying the source code.

You can add and update:

* Skills
* Projects
* Education
* Experience
* Contact messages

## Screenshots

Add screenshots of your portfolio here after completing the design.

```text
screenshots/
├── home.png
├── about.png
├── projects.png
└── contact.png
```

Example:

```markdown
![Portfolio Home](screenshots/home.png)
```

## Deployment

The portfolio can be deployed online using platforms such as Render.

After deployment, the live portfolio URL can be added to my resume and LinkedIn profile.

## Future Enhancements

* Custom domain
* PostgreSQL database
* Email notifications for contact messages
* Blog section
* Project search and filtering
* Google Analytics
* Improved animations
* CI/CD deployment

## Learning Outcomes

Through this project, I gained practical experience in:

* Django web development
* MTV architecture
* Django ORM
* Database management
* HTML, CSS and JavaScript
* Responsive web design
* Django Admin
* Form handling
* Static and media file management
* Git and GitHub
* Web application deployment

