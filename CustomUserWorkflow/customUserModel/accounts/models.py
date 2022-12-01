from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from accounts.userManager import CustomUserManager

# Create your models here.
GENDER_CHOICES = (
    ('m', "MALE"),
    ('f', "FEMALE"),
)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username            = models.CharField(max_length=50, unique=True)
    first_name          = models.CharField(max_length=30)
    last_name           = models.CharField(max_length=30)
    email               = models.EmailField(max_length=150, unique=True)
    phone               = models.CharField(max_length=15, unique=True)
    emailVarifiedCode   = models.CharField(max_length=6)
    profilePicture      = models.ImageField(upload_to="uploads/profilePicture")
    gender              = models.CharField(max_length=8, choices=GENDER_CHOICES, default='m')
    created_at          = models.DateTimeField(auto_now_add=True)
    last_updated_at     = models.DateTimeField(auto_now=True)
    is_varified         = models.BooleanField(default=False)
    is_admin            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=False)
    is_staff            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username