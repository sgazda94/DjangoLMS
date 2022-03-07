from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from dj_schulx.users.forms import UserAdminChangeForm, UserAdminCreationForm
from dj_schulx.users.models import Guardian, Manager, Student, Teacher, User

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]


class StudentAdmin(admin.ModelAdmin):
    pass


class GuardianAdmin(admin.ModelAdmin):
    pass


class TeacherAdmin(admin.ModelAdmin):
    pass


class ManagerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Student)
admin.site.register(Guardian)
admin.site.register(Teacher)
admin.site.register(Manager)
