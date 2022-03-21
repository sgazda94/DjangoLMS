from django.urls import path

from . import views

app_name = "school"

urlpatterns = [
    # path("", views.GroupListView.as_view(), name="group-list"),
    # group
    path("students/", views.StudentListView.as_view(), name="students-list"),
    path("teachers/", views.TeacherListView.as_view(), name="teachers-list"),
    path("guardians/", views.GuardianListView.as_view(), name="guardians-list"),
]
