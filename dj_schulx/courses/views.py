from courses.models import Category, Course, LessonScript
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from dj_schulx.courses.forms import LessonScriptForm


def index(request):
    return render(request, "base.html")


# Lesson
class LessonDetailView(LoginRequiredMixin, DetailView):
    model = LessonScript


class LessonCreateView(CreateView):
    model = LessonScript
    form_class = LessonScriptForm
    template_name = "courses/create_update_form.html"


class LessonUpdateView(LoginRequiredMixin, UpdateView):
    model = LessonScript
    form_class = LessonScriptForm
    template_name = "courses/create_update_form.html"


class LessonDeleteView(LoginRequiredMixin, DeleteView):
    model = LessonScript
    template_name = "courses/confirm_delete_form.html"
    success_url = reverse_lazy("accounts:index")


# Category
class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["courses_list"] = Course.objects.filter(category=self.get_object())
        return context


# Course
class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lesson_list"] = LessonScript.objects.filter(course=self.get_object())
        return context


class CourseListView(LoginRequiredMixin, ListView):
    model = Course
