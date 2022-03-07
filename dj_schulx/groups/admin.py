from django.contrib import admin

from .models import Group, Lesson


class GroupAdmin(admin.ModelAdmin):
    list_display = ("id", "course", "week_day")


admin.site.register(Group, GroupAdmin)


class LessonAdmin(admin.ModelAdmin):
    pass


admin.site.register(Lesson, LessonAdmin)
