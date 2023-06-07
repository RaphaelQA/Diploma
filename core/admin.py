from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    search_fields = ('username','first_name', 'last_name')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    list_display = ('username', 'email', 'first_name', 'last_name')
    exclude = ['password']
    readonly_fields = ('last_login', 'date_joined')

admin.site.register(User, UserAdmin)