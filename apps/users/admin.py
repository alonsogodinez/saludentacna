from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'], code='duplicate_username',)

@admin.register(User)
class UserAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    fieldsets = (
        ('Usuario',{'fields': ('username','password')}),
        ('Informacion Personal', {'fields': ('first_name',
                                             'last_name',
                                             'email',
                                             'avatar')}),
        ('Permisos',{'fields':('is_active',
                               'is_staff',
                               'is_superuser',
                               'groups',
                               'user_permissions')}),
    )
    add_fieldsets = (
        ('Usuario', {
            'classes': ('wide',),
            'fields': ('username',
                       'password1',
                       'password2',)
        }),

        ('Datos Personales', {
            'classes': ('wide',),
            'fields': ('first_name',
                       'last_name',
                       'email',)
        }))

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    pass

@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    pass