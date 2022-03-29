from datetime import date, timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from django.views.generic.edit import FormView

from dj_schulx.groups.forms import GroupForm, LessonForm, LessonStartForm
from dj_schulx.groups.models import Group, Lesson, StudentPresence
from dj_schulx.users.models import Teacher

# Group


class GroupDetailView(LoginRequiredMixin, DetailView):
    model = Group

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        group = self.get_object()
        lessons = Lesson.objects.filter(group=group)
        context["lesson_list"] = lessons
        students = group.students.all()
        for student in students:
            student.presences = StudentPresence.objects.filter(
                student=student
            ).order_by("lesson__number")
        context["students"] = students
        return context


class GroupListView(LoginRequiredMixin, ListView):
    model = Group


class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm
    template_name = "groups/group_form.html"


class GroupUpdateView(LoginRequiredMixin, UpdateView):
    model = Group
    fields = "__all__"
    template_name = "groups/group_form.html"


class GroupDeleteView(LoginRequiredMixin, DeleteView):
    model = Group
    template_name = "groups/confirm_delete_form.html"
    success_url = reverse_lazy("accounts:index")


# Lesson


class LessonDetailView(LoginRequiredMixin, DetailView):
    model = Lesson


class LessonCreateView(LoginRequiredMixin, CreateView):
    model = Lesson
    form_class = LessonForm
    template_name = "groups/lesson_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["group"] = Group.objects.get(pk=self.kwargs["group_id"])
        return context

    def get_initial(self):
        initial = super().get_initial()
        group = Group.objects.get(pk=self.kwargs["group_id"])
        teacher = Teacher.objects.get(user=self.request.user)
        initial["teacher"] = teacher
        initial["start_time"] = group.start_time
        initial["end_time"] = group.end_time
        last_lesson = Lesson.objects.filter(group=group).last()
        if last_lesson:
            initial["date"] = last_lesson.date + timedelta(days=7)
        else:
            initial["date"] = date.today()
        initial["group"] = group
        return initial

    def form_valid(self, form):
        lesson = form.save(commit=False)
        group = Group.objects.get(pk=self.kwargs["group_id"])
        last_lesson = Lesson.objects.filter(group=group).last()
        if last_lesson:
            lesson.number = last_lesson.number + 1
        else:
            lesson.number = 1
        lesson.group = group
        lesson.save()
        for student in group.students.all():
            StudentPresence.objects.create(student=student, lesson=lesson)
        return super().form_valid(form)


class LessonUpdateView(LoginRequiredMixin, UpdateView):
    model = Lesson
    fields = "__all__"
    template_name = "groups/lesson_form.html"


class LessonStartView(FormView):
    template_name = "groups/lesson_new.html"
    form_class = LessonStartForm

    def get_success_url(self):
        return reverse("groups:group-detail", kwargs={"pk": self.kwargs["group_id"]})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        lesson = Lesson.objects.get(pk=self.kwargs["pk"])
        kwargs["presences"] = StudentPresence.objects.filter(lesson=lesson.pk)
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lesson"] = Lesson.objects.get(pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        data = form.cleaned_data
        lesson = Lesson.objects.get(pk=self.kwargs["pk"])
        if lesson.is_started is False:
            lesson.is_started = True
        elif lesson.is_started is True:
            lesson.is_ended = True
        lesson.save()
        presences = StudentPresence.objects.filter(lesson=lesson.pk)
        for pk, is_present in data.items():
            presence = presences.get(id=pk)
            presence.is_present = is_present
            presence.save()
        return super().form_valid(form)
