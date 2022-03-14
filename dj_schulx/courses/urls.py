from django.urls import path

from . import views

app_name = "courses"

urlpatterns = [
    path("", views.CourseListView.as_view(), name="course-list"),
    # lesson
    path(
        "<slug:slug>/lesson/<int:pk>",
        views.LessonScriptDetailView.as_view(),
        name="lesson-script-detail",
    ),
    path(
        "<slug:slug>/lesson/create/",
        views.LessonScriptCreateView.as_view(),
        name="lesson-script-create",
    ),
    path(
        "<slug:slug>/lesson/<int:pk>/update/",
        views.LessonScriptUpdateView.as_view(),
        name="lesson-update",
    ),
    path(
        "<slug:slug>/lesson/<int:pk>/delete/",
        views.LessonScriptDeleteView.as_view(),
        name="lesson-script-delete",
    ),
    # category
    path(
        "category/<slug:slug>",
        views.CategoryDetailView.as_view(),
        name="category-detail",
    ),
    # course
    path("<slug:slug>", views.CourseDetailView.as_view(), name="course-detail"),
]
