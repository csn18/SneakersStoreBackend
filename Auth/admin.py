from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from Auth.forms import CustomUserCreationForm, CustomUserChangeForm
from Auth.models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    ordering = ['email']
    search_fields = ['email']
    list_display = ['email', 'is_staff', 'is_active']
    list_filter = ['email', 'is_staff', 'is_active']

    fieldsets = (
        (
            'Авторизация',
            {
                'fields': (
                    'email', 'password'
                )
            }
        ),
        (
            'Права доступа',
            {
                'fields': (
                    'is_staff', 'is_active'
                )
            }
        ),
    )
    add_fieldsets = (
        (
            None, {
                'classes': ['wide'],
                'fields': [
                    'email', 'password1', 'password2', 'is_staff',
                    'is_active'
                ]
            }
        ),
    )


admin.site.register(User, CustomUserAdmin)
