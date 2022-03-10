from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

from dj_schulx.users.models import User


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ["title"]
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Course(models.Model):
    owner = models.ForeignKey(
        User, related_name="courses_created", on_delete=models.RESTRICT
    )
    category = models.ForeignKey(
        Category, related_name="courses", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    overview = models.TextField()

    class Meta:
        ordering = ["category", "title"]

    def get_absolute_url(self):
        return reverse("courses:course-detail", args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class LessonScript(models.Model):
    course = models.ForeignKey(Course, related_name="courses", on_delete=models.CASCADE)
    course_order = models.SmallIntegerField()
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255, blank=True)
    content = MarkdownxField()

    def __str__(self):
        return self.title

    @property
    def formatted_markdown(self):
        return markdownify(self.content)

    def get_absolute_url(self):
        return reverse(
            "courses:lesson-script-detail",
            kwargs={"pk": self.id, "slug": self.course.slug},
        )
