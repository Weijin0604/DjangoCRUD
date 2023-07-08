from django.contrib import admin
from .models import User
# Register your models here.

class user(admin.ModelAdmin):
    list_display = ('username', 'password','create_date')
    exclude = ('create_date',)
admin.site.register(User,user)