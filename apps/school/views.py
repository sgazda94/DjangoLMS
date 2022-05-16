from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import FormView

from apps.groups.models import Group, Lesson, StudentPresence
from apps.school.forms import AddStudentToGroupForm
from apps.users.models import Guardian, Student, Teacher


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = "school/student_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        for obj in queryset:
            group = Group.objects.filter(students=obj).first()
            obj.group = group
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = AddStudentToGroupForm
        return context


class AddStudentToGroupView(FormView):
    success_url = "/school/students/"
    form_class = AddStudentToGroupForm

    def form_valid(self, form):
        data = form.cleaned_data
        group = data["group"]
        student = data["student"]
        if not group.students.filter(pk=student.pk).exists():
            group.students.add(student)
            lessons = Lesson.objects.filter(group=group.pk)
            for lesson in lessons:
                StudentPresence.objects.create(student=student, lesson=lesson)
        return super().form_valid(form)


class TeacherListView(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = "school/teacher_list.html"


class GuardianListView(LoginRequiredMixin, ListView):
    model = Guardian
    template_name = "school/guardian_list.html"
