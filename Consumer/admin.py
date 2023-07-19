from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from Auth.forms import CustomUserCreationForm, CustomUserChangeForm
from Consumer.models import Favorites, Geolocate, Address, Consumer

admin.site.register(Geolocate)
admin.site.register(Address)
admin.site.register(Favorites)


class AdminConsumer(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    fieldsets = (
        (
            'Авторизация', {
                'fields': [
                    'email', 'password'
                ]
            }
        ),
        (
            'Личные данные', {
                'fields': [
                    'phone', 'address', 'geolocate'
                ]
            }
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['email', 'password1', 'password2']
            }
        ),
    )

    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()


admin.site.register(Consumer, AdminConsumer)
