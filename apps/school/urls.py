from django.urls import path

from . import views

app_name = "school"

urlpatterns = [
    # path("", views.GroupListView.as_view(), name="group-list"),
    # group
    path("students/", views.StudentListView.as_view(), name="student-list"),
    path(
        "students/add-to-group",
        views.AddStudentToGroupView.as_view(),
        name="add-to-group",
    ),
    path("teachers/", views.TeacherListView.as_view(), name="teacher-list"),
    path("guardians/", views.GuardianListView.as_view(), name="guardian-list"),
]
