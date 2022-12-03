from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    # create user
    def create_user(self, email, username, phone, password=None):
        if not email:
            raise ValueError("Please Provide an Email Address")

        user = self.model(
            email = email,
            username = username,
            phone = phone,
            password = password,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user


    # create_superuser
    def create_superuser(self, email, username, phone, password):
        user = self.create_user(
            email = email,
            username=username,
            phone = phone,
            password = password,
        )

        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user