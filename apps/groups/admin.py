from django.contrib import admin

from .models import Group, Lesson, StudentPresence


class GroupAdmin(admin.ModelAdmin):
    list_display = ("id", "course", "week_day")


admin.site.register(Group, GroupAdmin)


class LessonAdmin(admin.ModelAdmin):
    pass


admin.site.register(Lesson, LessonAdmin)


class StudentPresenceAdmin(admin.ModelAdmin):
    list_display = ("lesson", "student")


admin.site.register(StudentPresence, StudentPresenceAdmin)
