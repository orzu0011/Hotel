
from django.contrib.auth.models import PermissionsMixin, AbstractUser, Group, Permission
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django_resized import ResizedImageField
from phone_field import PhoneField
from django.db import models


class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name="unique_group_set")
    user_permissions = models.ManyToManyField(Permission, related_name="unique_user_set")


class MyUserManager(BaseUserManager):
    """
    However, in Django REST Framework (DRF), the term "Users"
    typically refers to the authentication and authorization
    system provided by DRF. DRF provides built-in views and
    serializers for user registration, login, and other
    user-related operations. This BaseUserManager for my
    User models operate the users ever for customer.
    """

    def create_user(self, username, password=None, **extra_fields):
        """
        This function create user automatically.
        """
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.save()
        return user

    def _create_user(self, username, password=None, **extra_fields):
        """
        This function create user automatically.
        """
        user = self.model(username=username, **extra_fields)
        user.is_active = True
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(username, password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE = (
        ('director', 'Director'),
        ('admin', 'Admin'),
        ('seller', 'Sotuvchi'),
        ('customer', 'Mijoz'),
    )
    custom_user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, verbose_name="Пользовательский пользователь")
    first_name = models.CharField(verbose_name="Ism", max_length=255, blank=True)
    last_name = models.CharField(verbose_name="Familiya", max_length=255, blank=True)
    avatar = ResizedImageField(verbose_name="Rasm", size=[600, 400],
                                crop=['middle', 'center'],
                                null=True, blank=True,
                                upload_to="user_avatars")
    email = models.EmailField(verbose_name="Pochta", unique=True, blank=True)
    username = models.CharField(verbose_name="username", max_length=255, unique=True)
    is_staff = models.BooleanField(verbose_name="Xodimlarning holati", default=False)
    is_active = models.BooleanField(verbose_name="Faol holatdami", default=True, )
    birthday = models.DateField(verbose_name="Tug'ilgan kun", null=True, blank=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    user_type = models.CharField(verbose_name="Foydalanuvchi turi", max_length=255, choices=USER_TYPE, default='seller')

    USERNAME_FIELD = "username"
    objects = MyUserManager()

    def __str__(self):
        return self.username

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"


class ViewPermission(models.Model):
    view_name = models.CharField(verbose_name="Класс отображения", max_length=255)
    path_name = models.CharField(verbose_name="URL Name", max_length=255, null=True, blank=True)
    method = models.CharField(verbose_name="Uslub/Usul", max_length=255, default="post")

    class Meta:
        # verbose_name = "Разрешение на просмотр"
        # verbose_name_plural = "Просмотр разрешений"
        ordering = "view_name",

    def __str__(self):
        return f"{self.path_name} - {self.view_name} - {self.method}"