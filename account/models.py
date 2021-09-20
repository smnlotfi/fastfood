from django.db import models
from  django.contrib.auth.models import BaseUserManager,AbstractBaseUser,AbstractUser
# Create your models here.



class MyUserManager(BaseUserManager):

    def create_user(self,mobile,password=None):
        if not mobile:
            raise ValueError('شماره موبایل خود را وارد نمایید')

        user=self.model(
            mobile=mobile,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,mobile,password=None):
        user=self.create_user(
            mobile,
            password=password,

        )
        user.is_admin=True
        user.is_superuser=True
        user.save(using=self._db)
        return user



class MyUser(AbstractBaseUser):
    mobile=models.CharField(verbose_name='شماره موبایل',max_length=11,unique=True)
    name=models.CharField(verbose_name='نام',max_length=50)
    adress=models.TextField(verbose_name='آدرس',max_length=300)
    created_at=models.DateTimeField(verbose_name='تاریخ ثبت نام',auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='آخرین ورود',auto_now=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    sms_code=models.CharField(max_length=4,null=True,blank=True)

    USERNAME_FIELD='mobile'
    objects=MyUserManager()


    class Meta:
        verbose_name='کاربر'
        verbose_name_plural='کاربر ها'

    def __str__(self):
        return self.name

    def has_perm(self,perm,object=None):
        return True

    def has_module_perms(self, app_label):
        return True;

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
