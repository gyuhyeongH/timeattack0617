from django.contrib import admin
from user.models import User as UserModel
from user.models import UserType, UserLog
# Register your models here.


admin.site.register(UserModel)
admin.site.register(UserType)
admin.site.register(UserLog)