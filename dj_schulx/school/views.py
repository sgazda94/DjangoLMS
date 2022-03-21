from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from dj_schulx.groups.models import Group
from dj_schulx.users.models import Guardian, Student, Teacher


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = "school/student_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        for obj in queryset:
            group = Group.objects.get(students=obj)
            obj.group = group
        return queryset


class TeacherListView(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = "school/teacher_list.html"


class GuardianListView(LoginRequiredMixin, ListView):
    model = Guardian
    template_name = "school/guardian_list.html"
