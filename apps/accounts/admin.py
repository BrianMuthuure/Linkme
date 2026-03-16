from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import User, Profile
from .forms import UserCreationForm, UserChangeForm


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    readonly_fields = ['date_joined', 'last_login', 'verified_at']

    list_display = [
        'email', 
        'is_admin', 
        'is_verified', 
        'verified_at', 
        'date_joined'
        ]
    
    list_filter = ['is_admin', 'is_verified']
    fieldsets = [
        (None, {'fields': ['email', 'password']}),
        ('Permissions', {'fields': ['is_admin', 'is_verified']}),
        ('Dates', {'fields': ['date_joined', 'last_login', 'verified_at']}),
    ]
    add_fieldsets = [
        (None, {
            'classes': ['wide'],
            'fields': ['email', 'password1', 'password2'],
        }),
    ]
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = []  


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'bio', 'date_of_birth', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['user__email', 'name', 'bio']
    readonly_fields = ['created_at', 'updated_at']