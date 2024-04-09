from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class Gender:
    MALE = "M"
    FEMALE = "F"
    OTHER = "O"

    GENDER_CHOICE = [
        (FEMALE, "Female"),
        (MALE, "Male"),
        (OTHER, "Other"),
    ]
    GENDER_DICT = dict(GENDER_CHOICE)

class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    prefix = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    nickname = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    th_first_name = models.CharField(max_length=255, null=True, blank=True)
    th_last_name = models.CharField(max_length=255, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=255, choices=Gender.GENDER_CHOICE)


class Teacher(models.Model):
    abstract_user = models.OneToOneField(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE)
    id_card_number = models.CharField(max_length=255)
    info = models.CharField(max_length=1024)
    image_url = models.CharField(max_length=1024, null=True, blank=True)
    joined_date = models.DateField(default=timezone.now)

    def __str__ (self) -> str:
        return self.abstract_user.first_name + " " + self.abstract_user.last_name

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    student_id = models.CharField(max_length=255)
    remark = models.CharField(max_length=1024)
    joined_date = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

class Parents(models.Model):
    abstract_user = models.OneToOneField(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE)
    parent_id = models.CharField(max_length=255)
    student = models.ManyToManyField(Student)
    relation = models.CharField(max_length=255, default="Parent")
    joined_date = models.DateField(default=timezone.now)