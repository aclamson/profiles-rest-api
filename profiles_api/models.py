from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

# model manager class
class UserProfileManager(BaseUserManager):
    """Manger for user profiles. Contains functions for managing the user profiles."""
    
    def create_user(self, email, name, password=None):
        """Create and save a new user profile with given details."""
        if not email:
            raise ValueError("Users must have an email address.")

        # normalize the email address
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        # hash password in the model
        # django does this by default with set_password function
        user.set_password(password)
        user.save(using=self._db) 

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new super user with given details."""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

# Create model
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""

    # Fields for the database and properties of the UserProfile object
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Custom model manager
    objects = UserProfileManager()

    # Helps to work with django admin
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    #UserProfile functions
    def get_full_name(self):
        """Retrieve full name of the user"""
        return self.name
    
    def get_short_name(self):
        """Retrieve short name of the user"""
        return self.name
    
    def __str__(self):
        """Return string representation of the user"""
        return self.email
    

class ProfileFeedItem(models.Model):
    """Profile status update"""

    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.status_text