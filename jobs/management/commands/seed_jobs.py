from django.core.management.base import BaseCommand
from jobs.models import Job
from django.contrib.auth import get_user_model
import random

User = get_user_model()

SAMPLE = [
    ("Frontend Developer","Andela","Lagos","Tech"),
    ("Backend Engineer","Paystack","Lagos","Tech"),
    ("Product Designer","Flutterwave","Abuja","Design"),
    ("Marketing Executive","Konga","Lagos","Marketing"),
    ("Financial Analyst","GTBank","Lagos","Finance"),
    ("Legal Counsel","Access Bank","Lagos","Legal"),
    ("Data Scientist","Interswitch","Lagos","Tech"),
    ("UI Designer","Hotels.ng","Lagos","Design"),
    ("Growth Marketer","PiggyVest","Lagos","Marketing"),
    ("Accountant","UBA","Lagos","Finance"),
    ("HR Manager","MTN Nigeria","Lagos","Finance"),
    ("DevOps Engineer","Andela","Lagos","Tech"),
    ("Mobile Developer","Jumia","Lagos","Tech"),
    ("Content Strategist","Pulse","Lagos","Marketing"),
    ("Compliance Officer","Sterling Bank","Lagos","Legal"),
    ("QA Engineer","Kuda","Lagos","Tech"),
    ("Graphic Designer","Zinox","Ibadan","Design"),
    ("Sales Executive","Slot","Ibadan","Marketing"),
    ("Business Analyst","Zenith Bank","Abuja","Finance"),
    ("Contract Lawyer","LegalHub","Lagos","Legal"),
]

class Command(BaseCommand):
    help = 'Seed the database with sample jobs'

    def handle(self, *args, **options):
        user, _ = User.objects.get_or_create(username='employer', defaults={'email':'employer@example.com'})
        user.set_password('password123')
        user.save()
        Job.objects.all().delete()
        for title, company, location, category in SAMPLE:
            Job.objects.create(
                owner=user,
                title=title,
                company=company,
                location=location,
                job_type=random.choice(['FT','RM','CT']),
                salary_min=random.randint(50000,200000),
                salary_max=random.randint(200001,500000),
                description=f"{title} role at {company} in {location}. Responsibilities include ...",
                category=category,
                is_active=True
            )
        self.stdout.write(self.style.SUCCESS('Seeded jobs successfully.'))
