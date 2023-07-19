from django.contrib.auth.forms import UserCreationForm, UserChangeForm, \
    ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.forms import CharField, PasswordInput

from Auth.models import User


class CustomUserCreationForm(UserCreationForm):
    password1 = CharField(label='Password', widget=PasswordInput)
    password2 = CharField(label='Password confirmation', widget=PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError('Passwords dont match')
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['email']


class CustomUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['email', 'password']

    def clean_password(self):
        return self.initial['password']
