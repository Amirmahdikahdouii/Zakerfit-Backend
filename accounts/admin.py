from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import User, PhoneNumberValidation
from django.contrib.auth.models import Group


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ("phone_number", "first_name", "last_name", "gender", 'is_admin')
    list_filter = ("gender", "is_admin")
    fieldsets = (
        (None, {"fields": ("phone_number", "email", "password")}),
        ("Personal Information", {"fields": ("first_name", "last_name", "age", "gender")}),
        ("Permissions", {"fields": ("is_admin",)})
    )

    add_fieldsets = (
        (None,
         {"fields": ("phone_number", "email", "first_name", "last_name", "gender", "age", "password1", "password2")}),
    )
    ordering = ['id']
    search_fields = ("phone_number", "first_name", "last_name")
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)


class PhoneNumberValidationAdmin(admin.ModelAdmin):
    class Meta:
        model = PhoneNumberValidation

    list_display = ("phone_number", "validation_code")
    ordering = ("-creation_date",)


admin.site.register(PhoneNumberValidation, PhoneNumberValidationAdmin)
