from django.db import models
from django.db.models import DO_NOTHING
from django.urls import reverse

from dj_schulx.courses.models import Course, LessonScript
from dj_schulx.users.models import Student, Teacher

# Archwizacja grupy?
# from django.core.exceptions import ValidationError


class Group(models.Model):
    teacher = models.ForeignKey(
        Teacher, on_delete=models.SET_NULL, blank=True, null=True
    )
    students = models.ManyToManyField(Student, blank=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    # school

    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    WEEK_DAY_CHOICES = (
        (MONDAY, "Monday"),
        (TUESDAY, "Tuesday"),
        (WEDNESDAY, "Wednesday"),
        (THURSDAY, "Thursday"),
        (FRIDAY, "Friday"),
        (SATURDAY, "Saturday"),
    )
    week_day = models.SmallIntegerField(choices=WEEK_DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def get_absolute_url(self):
        return reverse("groups:group-detail", kwargs={"pk": self.id})

    def __str__(self):
        return f"{self.get_week_day_display()} /  {self.course} /  {self.start_time} - {self.end_time} "


class Lesson(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, unique=False)
    number = models.SmallIntegerField(default=None)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.SET_NULL, blank=True, null=True, unique=False
    )
    lesson_script = models.ForeignKey(
        LessonScript, on_delete=models.SET_NULL, blank=True, null=True
    )
    date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    is_started = models.BooleanField(default=False)
    is_ended = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.group} / {self.number}"

    def get_absolute_url(self):
        group_id = self.group.pk
        return reverse(
            "groups:lesson-detail", kwargs={"pk": self.pk, "group_id": group_id}
        )

    # def clean(self):
    #     if self.start_date >= self.end_date:
    #         raise ValidationError("End date cannot be before start date")


class StudentPresence(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=DO_NOTHING,
    )
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    is_present = models.BooleanField(default=False)
