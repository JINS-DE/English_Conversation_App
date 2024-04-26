from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Users(AbstractUser):
    # CEFR 레벨 선택지를 정의
    LEVEL_CHOICES = [
        ('A1', 'Beginner'),
        ('A2', 'Elementary'),
        ('B1', 'Intermediate'),
        ('B2', 'Upper Intermediate'),
        ('C1', 'Advanced'),
        ('C2', 'Proficiency')
    ]
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES, default='A1', verbose_name="CEFR Level")
    profile_img = models.ImageField(upload_to='profile_images/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.username