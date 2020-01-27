from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    GENDER_CHOICES = [("male", "Male"), ("female", "Female"), ("not-specified", "Not specified")]

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    website = models.URLField(_("website"), max_length=200, null=True)
    bio = models.TextField(_("bio"), null=True)
    phone = models.CharField(_("phone number"), max_length=140, null=True)
    gender = models.CharField(_("gender"), max_length=80, choices=GENDER_CHOICES, null=True)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
