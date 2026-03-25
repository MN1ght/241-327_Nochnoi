import os
import sys
import django
import random
from datetime import date, timedelta

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab1.settings')
django.setup()

from faker import Faker
from mainapp.models import Client

fake = Faker('ru_RU')
SUBS = ['basic', 'standard', 'premium']

for _ in range(20):
    Client.objects.create(
        full_name=fake.name(),
        phone=fake.phone_number(),
        email=fake.unique.email(),
        birth_date=fake.date_of_birth(minimum_age=18, maximum_age=60),
        subscription_type=random.choice(SUBS),
        subscription_end=date.today() + timedelta(days=random.randint(1, 365)),
        is_active=random.choice([True, False]),
        visits_count=random.randint(0, 200),
    )

print("Готово! Создано 20 клиентов.")