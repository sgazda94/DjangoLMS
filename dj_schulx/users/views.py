from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    RedirectView,
    UpdateView,
)

from .forms import GuardianCreationForm, ManagerCreationForm, TeacherCreationForm
from .models import Guardian, Manager, Student, Teacher, User

# cookiecutter-django

active_User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = active_User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = active_User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


def index(request):

    return render(request, "base.html")


# STUDENT
class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    fields = "__all__"
    template_name = "users/create_update_form.html"


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    fields = (
        "__all__"  # Not recommended (potential security issue if more fields added)
    )
    template_name = "users/create_update_form.html"


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy("index")


# GUARDIAN
class GuardianDetailView(LoginRequiredMixin, DetailView):
    model = Guardian

    def get_context_data(self, **kwargs):
        context = super(GuardianDetailView, self).get_context_data(**kwargs)
        context["student_list"] = Student.objects.filter(guardian=self.get_object())
        return context


class GuardianCreateView(CreateView):
    model = User
    form_class = GuardianCreationForm
    template_name = "users/create_update_form.html"

    def form_valid(self, form):
        user = form.save()
        return redirect("users:index")


class GuardianUpdateView(LoginRequiredMixin, UpdateView):
    model = Guardian
    fields = "__all__"
    template_name = "users:create_update_form.html"


class GuardianDeleteView(LoginRequiredMixin, DeleteView):
    model = Guardian
    success_url = reverse_lazy("index")
    template_name = "users:confirm_delete_form.html"


# TEACHER


class TeacherDetailView(LoginRequiredMixin, DetailView):
    model = Teacher


class TeacherCreateView(CreateView):
    model = User
    form_class = TeacherCreationForm
    template_name = "users/create_update_form.html"

    def form_valid(self, form):
        user = form.save()
        return redirect("users:index")


class TeacherUpdateView(LoginRequiredMixin, UpdateView):
    model = Teacher
    fields = "__all__"
    template_name = "users/create_update_form.html"


class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    model = Teacher
    template_name = "users/confirm_delete_form.html"
    success_url = reverse_lazy("users:index")


# MANAGER


class ManagerDetailView(LoginRequiredMixin, DetailView):
    model = Manager


class ManagerCreateView(CreateView):
    model = User
    form_class = ManagerCreationForm
    template_name = "users/create_update_form.html"

    def form_valid(self, form):
        user = form.save()
        return redirect("users:index")


class ManagerUpdateView(LoginRequiredMixin, UpdateView):
    model = Manager
    fields = "__all__"
    template_name = "users/create_update_form.html"


class ManagerDeleteView(LoginRequiredMixin, DeleteView):
    model = Manager
    template_name = "users/confirm_delete_form.html"
    success_url = reverse_lazy("users:index")
