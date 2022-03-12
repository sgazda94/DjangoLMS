from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from dj_schulx.groups.forms import GroupForm, LessonForm
from dj_schulx.groups.models import Group, Lesson

active_user = get_user_model()
# Group


class GroupDetailView(LoginRequiredMixin, DetailView):
    model = Group

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lesson_list"] = Lesson.objects.filter(group=self.get_object())
        return context


class GroupListView(LoginRequiredMixin, ListView):
    model = Group


class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm
    template_name = "groups/create_update_form.html"


class GroupUpdateView(LoginRequiredMixin, UpdateView):
    model = Group
    fields = "__all__"
    template_name = "groups/create_update_form.html"


class GroupDeleteView(LoginRequiredMixin, DeleteView):
    model = Group
    template_name = "groups/confirm_delete_form.html"
    success_url = reverse_lazy("accounts:index")


# Lesson


class LessonDetailView(LoginRequiredMixin, DetailView):
    model = Lesson

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['lesson_list'] = Lesson.objects.filter(group=self.get_object())
        return context


@login_required
def create_lesson(request, group_id):
    if request.method == "POST":
        form = LessonForm(request.POST)

        if form.is_valid():
            lesson = form.save(commit=False)
            group = Group.objects.get(id=group_id)
            lesson.group = group
            last_lesson_number = Lesson.objects.filter(group=group_id)
            if last_lesson_number:
                last_lesson_number = last_lesson_number.latest("number").number
                lesson.number = last_lesson_number + 1
            else:
                lesson.number = 1
            lesson.save()
            return HttpResponseRedirect(
                reverse("groups:lesson-detail", kwargs={"pk": lesson.id})
            )
    else:
        form = LessonForm(user=active_user, group=group_id)

    return render(request, "groups/create_update_form.html", {"form": form})


class LessonUpdateView(LoginRequiredMixin, UpdateView):
    model = Lesson
    fields = "__all__"
    template_name = "groups/create_update_form.html"
