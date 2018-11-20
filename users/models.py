from django.db import models
from django.contrib.auth.models import User
from department.models import Department
from housing.models import House


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")
    department = models.ForeignKey(Department, blank=True, related_name="user")
    viewed_houses = models.ManyToManyField(House, blank=True, related_name="viewed_user")

    def __str__(self):
        if self.user.first_name or self.user.last_name:
            return self.user.first_name + " " + self.user.last_name
        return self.user.email

