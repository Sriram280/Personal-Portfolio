from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField(default=80)
    category = models.CharField(max_length=100, default="Technical")

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=300)
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title


class Education(models.Model):
    degree = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    year = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.degree


class Experience(models.Model):
    role = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.role


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True
    )

    def __str__(self):
        return f"{self.name} - {self.email}"