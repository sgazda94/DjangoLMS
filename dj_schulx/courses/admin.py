from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Category, Course, LessonScript


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class LessonScriptAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(LessonScript, MarkdownxModelAdmin)
