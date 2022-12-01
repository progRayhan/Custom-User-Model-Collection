from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):

    def create_user(self, email, username, phone, password=None):
        if not email:
            raise ValueError("Please provide an email address")

        if not username:
            raise ValueError("Please provide a username")

        if not phone:
            raise ValueError("Please provide a phone number")

        user = self.model(
            email = email,
            username = username,
            phone = phone,
            password = password
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, username, password):
        user = self.create_user(email=email, username=username, phone="01942831359", password=password)

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user