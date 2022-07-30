from django.contrib.auth.base_user import BaseUserManager


class SchoolManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff to be True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser to be True')

        return self.create_user(email, password, **extra_fields)
