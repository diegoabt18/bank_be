from django.contrib import admin
from .models.user import User
from .models.account import Account
from .models.register_user import Register_user

admin.site.register(User)
admin.site.register(Account)
admin.site.register(Register_user)

