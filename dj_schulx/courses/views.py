from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from dj_schulx.courses.forms import LessonScriptForm
from dj_schulx.courses.models import Category, Course, LessonScript


# from django.shortcuts import render
# Lesson
class LessonScriptDetailView(LoginRequiredMixin, DetailView):
    model = LessonScript
    template_name = "courses/lesson_detail.html"


class LessonScriptCreateView(CreateView):
    model = LessonScript
    form_class = LessonScriptForm
    template_name = "courses/lesson_script_form.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context["course"] = Course.objects.filter(category=self.get_object())
    #     return context

    def get_initial(self):
        print(self.request.GET)
        initial = super().get_initial()
        course = Course.objects.filter(slug=self.kwargs["slug"]).first()
        initial["course"] = course
        last_lesson_script_order = LessonScript.objects.filter(course=course)
        if last_lesson_script_order:
            last_lesson_script_order = last_lesson_script_order.latest(
                "course_order"
            ).course_order
            last_lesson_script_order += 1
        else:
            last_lesson_script_order = 1
        initial["course_order"] = last_lesson_script_order
        return initial

    def form_valid(self, form):
        data = self.request.POST
        course_id = data["course"]
        course_order = data["course_order"]
        course = Course.objects.filter(id=course_id).first()
        if LessonScript.objects.filter(
            course=course, course_order=course_order
        ).exists():
            form.errors[
                "course_order"
            ] = "Lesson Script with that number is already created"
            return self.form_invalid(form)
        else:
            return super().form_valid(form)


class LessonScriptUpdateView(LoginRequiredMixin, UpdateView):
    model = LessonScript
    form_class = LessonScriptForm
    template_name = "courses/lesson_script_form.html"


class LessonScriptDeleteView(LoginRequiredMixin, DeleteView):
    model = LessonScript
    template_name = "courses/confirm_delete_form.html"
    success_url = reverse_lazy("users:index")


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
        context["lesson_list"] = LessonScript.objects.filter(
            course=self.get_object()
        ).order_by("course_order")
        context["slug"] = self.kwargs["slug"]
        return context


class CourseListView(LoginRequiredMixin, ListView):
    model = Course
