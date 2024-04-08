from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Teacher, Student, Parents

class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "password",
            "gender",
            "email",
            "is_superuser",
            "is_staff",
            "is_active",
            "date_joined",
        )


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = [
        'username',
        'email',
        'first_name',
        'last_name'
    ]
    readonly_fields = ("date_joined",)
    fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password",
                    "nickname",
                    "first_name",
                    "last_name",
                    "th_first_name",
                    "th_last_name",
                    "gender",
                    "email",
                    "birth_date",
                    "is_superuser",
                    "is_staff",
                    "is_active",
                    "date_joined",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        "get_user_username",
        "get_user_nickname",
        "get_user_first_name",
        "get_user_last_name",
    )

    @admin.display(description="Username")
    def get_user_username(self, obj):
        return obj.abstract_user.username

    @admin.display(description="Nickname")
    def get_user_nickname(self, obj):
        return obj.abstract_user.nickname

    @admin.display(description="First Name")
    def get_user_first_name(self, obj):
        return obj.abstract_user.first_name

    @admin.display(description="Last Name")
    def get_user_last_name(self, obj):
        return obj.abstract_user.last_name


@admin.register(Parents)
class ParentsAdmin(admin.ModelAdmin):
    list_display = (
        "get_user_username",
        "get_user_nickname",
        "get_user_first_name",
        "get_user_last_name",
    )

    @admin.display(description="Username")
    def get_user_username(self, obj):
        return obj.abstract_user.username

    @admin.display(description="Nickname")
    def get_user_nickname(self, obj):
        return obj.abstract_user.nickname

    @admin.display(description="First Name")
    def get_user_first_name(self, obj):
        return obj.abstract_user.first_name

    @admin.display(description="Last Name")
    def get_user_last_name(self, obj):
        return obj.abstract_user.last_name
    

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "student_id",
        "joined_date",
    ]
