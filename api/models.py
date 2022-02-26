import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager,
	PermissionsMixin
)


def upload_to_path(instance, filename):
	return u'web/mediafiles/%s/%s' % (str(instance.id), filename)


# Create your models here.
class UserProfileManager(BaseUserManager):

	def _create_user(self, email: str, first_name: str, password, **optional_fields):
		values = [email, first_name]
		field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
		for field_name, value in field_value_map.items():
			if not value:
				raise ValueError('The {} value must be set'.format(field_name))

		email = self.normalize_email(email)
		user = self.model(email=email, first_name=first_name, **optional_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email: str, first_name: str, password=None, **optional_fields):
		optional_fields.setdefault('is_staff', False)
		optional_fields.setdefault('is_superuser', False)

		return self._create_user(email, first_name, password, **optional_fields)


	def create_superuser(self, email: str, first_name: str, password=None, **optional_fields):
		optional_fields.setdefault('is_staff', True)
		optional_fields.setdefault('is_superuser', True)

		if optional_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')
		if optional_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')

		return self._create_user(email, first_name, password, **optional_fields)


class UserProfile(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(max_length=255, unique=True)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255, blank=True, null=True)
	date_of_birth = models.DateField(blank=True, null=True)
	profile_picture = models.ImageField(blank=True, null=True, upload_to=upload_to_path)
	date_joined = models.DateTimeField(default=timezone.now)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	objects = UserProfileManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name']

	def full_name(self) -> str:
		if self.last_name:
			return f"{self.first_name} {self.last_name}"
		return self.get_short_name()

	def get_short_name(self) -> str:
		return self.first_name

	def age(self):
		return int((datetime.date.today() - self.date_of_birth).days / 365.25)

	def __str__(self) -> str:
		return self.email
