from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
    # create_user
    def create_user(self, email, username, phone, fvrtColor, password=None):
        if not email:
            raise ValueError("Please Provide an Email Address")

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            phone=phone,
            fvrtColor=fvrtColor,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    # create_superuser
    def create_superuser(self, email, username, phone, fvrtColor, password):
        user = self.create_user(email, username, phone, fvrtColor, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user 
        

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=155, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, unique=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    gender = models.CharField(max_length=8, choices=GENDER_CHOICES, default='M')
    profilePicture = models.ImageField(upload_to="uploads/profilePicture")
    address = models.CharField(max_length=150)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    fvrtColor = models.CharField(max_length=100)
    verify_code = models.CharField(max_length=10)

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone', 'fvrtColor']

    def __str__(self):
        return self.username