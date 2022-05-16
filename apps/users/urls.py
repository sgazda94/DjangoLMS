from django.urls import path

from . import views

# from apps.users.views import (
#     user_detail_view,
#     user_redirect_view,
#     user_update_view,
# )


app_name = "users"
urlpatterns = [
    path("~redirect/", view=views.user_redirect_view, name="redirect"),
    path("~update/", view=views.user_update_view, name="update"),
    path("<str:username>/", view=views.user_detail_view, name="detail"),
]

users_urlspatterns = [
    path("", views.index, name="index"),
    # Student
    path("student/<int:pk>", views.StudentDetailView.as_view(), name="student-detail"),
    path("student/create/", views.StudentCreateView.as_view(), name="student-create"),
    path(
        "student/<int:pk>/update/",
        views.StudentUpdateView.as_view(),
        name="student-update",
    ),
    path(
        "student/<int:pk>/delete/",
        views.StudentDeleteView.as_view(),
        name="student-delete",
    ),
    # Guardian
    path(
        "guardian/<int:pk>", views.GuardianDetailView.as_view(), name="guardian-detail"
    ),
    path(
        "guardian/create/", views.GuardianCreateView.as_view(), name="guardian-create"
    ),
    path(
        "guardian/<int:pk>/update/",
        views.GuardianUpdateView.as_view(),
        name="guardian-update",
    ),
    path(
        "guardian/<int:pk>/delete/",
        views.GuardianDeleteView.as_view(),
        name="guardian-delete",
    ),
    # Teacher
    path("teacher/<int:pk>", views.TeacherDetailView.as_view(), name="teacher-detail"),
    path("teacher/create/", views.TeacherCreateView.as_view(), name="teacher-create"),
    path(
        "teacher/<int:pk>/update/",
        views.TeacherUpdateView.as_view(),
        name="teacher-update",
    ),
    path(
        "teacher/<int:pk>/delete/",
        views.TeacherDeleteView.as_view(),
        name="teacher-delete",
    ),
    # Manager
    path("manager/<int:pk>", views.ManagerDetailView.as_view(), name="manager-detail"),
    path("manager/create/", views.ManagerCreateView.as_view(), name="manager-create"),
    path(
        "manager/<int:pk>/update/",
        views.ManagerUpdateView.as_view(),
        name="manager-update",
    ),
    path(
        "manager/<int:pk>/delete/",
        views.ManagerDeleteView.as_view(),
        name="manager-delete",
    ),
]

urlpatterns += users_urlspatterns
