from django.db import models


class Client(models.Model):

    SUBSCRIPTION_CHOICES = [
        ('basic', 'Базовый'),
        ('standard', 'Стандарт'),
        ('premium', 'Премиум'),
    ]

    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    birth_date = models.DateField()
    subscription_type = models.CharField(
        max_length=20,
        choices=SUBSCRIPTION_CHOICES,
        default='basic'
    )
    subscription_end = models.DateField()
    is_active = models.BooleanField(default=True)
    visits_count = models.IntegerField(default=0)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['full_name']