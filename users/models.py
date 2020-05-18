from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail

# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email, password):
        """ 
        Creates and saves a User with the given username, email 
        and password.
        """
        if not username:
            raise ValueError(_('Users must have an username'))
        if not email:
            raise ValueError(_('Users must have an email address'))

        username = self.model.normalize_username(username)
        email = self.normalize_email(email)

        user = self.model(
            username=username,
            email=email,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given username,
        email and password.
        """
        user = self.create_user(
            username,   # username=username
            email,
            password,    # password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'), 
        max_length=50,
        validators=[username_validator],
        unique=True
    )
    email = models.EmailField(_('email address'), unique=True)
    is_active = models.BooleanField(
        _('active'), 
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        )
    )
    is_staff = models.BooleanField(
        _('staff status'), 
        default=False, 
        help_text=_('Designates whether the user can log into this admin site.')
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        """ Send an email to this user. """
        send_mail(subject, message, from_email, [self.email], **kwargs)