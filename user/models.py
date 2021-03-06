from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an username')
        user = self.model(
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # python manage.py createsuperuser 사용 시 해당 함수가 사용됨
    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


# custom user model
class User(AbstractBaseUser):
    username = models.CharField("이름", max_length=50, null=True)
    password = models.CharField("비밀번호", max_length=128)
    email = models.EmailField("이메일 주소", max_length=100, unique=True)
    usertype = models.ForeignKey('UserType', on_delete=models.SET_NULL, null=True, related_name='type')


    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class UserType(models.Model):
    usertype = models.CharField("유저 타입", max_length=20)

    def __str__(self):
        return self.usertype


class UserLog(models.Model):
    user = models.OneToOneField(User, verbose_name="유저", on_delete=models.CASCADE)
    last_login = models.DateTimeField(auto_now=True)
    last_Apply = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email