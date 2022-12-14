from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class ProfileManager(BaseUserManager):
    # create user
    def create_user(self, email, first_name, last_name, phone, password=None):
        if not email:
            raise ValueError("Please provide an email address")

        email = self.normalize_email(email)

        user = self.model(
            email = email,
            first_name = first_name,
            last_name = last_name,
            phone = phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    # create superuser
    def create_superuser(self, email, first_name, last_name, phone, password):
        user = self.create_user(email, first_name, last_name, phone, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Profile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=150, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=8, choices=GENDER_CHOICES, default='M')
    picture = models.ImageField(upload_to="uploads/photoes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_verified = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    objects = ProfileManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']


    def __str__(self):
        return self.first_name + ' ' + self.last_name