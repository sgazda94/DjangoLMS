from django.urls import path

from . import views

app_name = "groups"

urlpatterns = [
    path("", views.GroupListView.as_view(), name="group-list"),
    # group
    path("<int:pk>", views.GroupDetailView.as_view(), name="group-detail"),
    path("create/", views.GroupCreateView.as_view(), name="group-create"),
    path("<int:pk>/update/", views.GroupUpdateView.as_view(), name="group-update"),
    path("<int:pk>/delete/", views.GroupDeleteView.as_view(), name="group-delete"),
    # lesson
    path(
        "<int:group_id>/lesson/<int:pk>",
        views.LessonDetailView.as_view(),
        name="lesson-detail",
    ),
    path(
        "<int:group_id>/lesson/create/",
        views.LessonCreateView.as_view(),
        name="lesson-create",
    ),
    path(
        "<int:group_id>/lesson/<int:pk>/update/",
        views.LessonUpdateView.as_view(),
        name="lesson-update",
    ),
    path(
        "<int:group_id>/lesson/<int:pk>/start",
        views.LessonStartView.as_view(),
        name="lesson-start",
    ),
]
