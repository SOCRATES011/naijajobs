from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

JOB_TYPE_CHOICES = [
    ('FT', 'Full-time'),
    ('PT', 'Part-time'),
    ('CT', 'Contract'),
    ('RM', 'Remote'),
]

CATEGORY_CHOICES = [
    ('Tech', 'Tech'),
    ('Design', 'Design'),
    ('Marketing', 'Marketing'),
    ('Finance', 'Finance'),
    ('Legal', 'Legal'),
]

class Job(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    job_type = models.CharField(max_length=2, choices=JOB_TYPE_CHOICES, default='FT')
    salary_min = models.PositiveIntegerField(null=True, blank=True)
    salary_max = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Tech')
    date_posted = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return f"{self.title} at {self.company}"
