from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, is_admin=False, 
        is_staff=False, is_active=True):

        if not email:
            raise ValueError("User must have mail")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email)
        )

        user.email = email
        user.set_password(password)
        user.is_admin = is_admin
        user.is_staff = is_staff
        user.is_active = is_active

        user.save(using=self._db)
        return user

    def create_staff_user(self, email, password):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
        )
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True, 
        )
        return user
