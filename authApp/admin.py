from django.contrib import admin
from .models.user import User
from .models.profile import Profile
from .models.product import Product

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Product)