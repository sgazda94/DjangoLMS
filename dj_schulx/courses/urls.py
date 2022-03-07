from django.urls import path

from . import views

app_name = "courses"

urlpatterns = [
    path("", views.CourseListView.as_view(), name="course-list"),
    # lesson
    path(
        "<slug:slug>/lesson/<int:pk>",
        views.LessonDetailView.as_view(),
        name="lesson-detail",
    ),
    path("lesson/create/", views.LessonCreateView.as_view(), name="lesson-create"),
    path(
        "<slug:slug>/lesson/<int:pk>/update/",
        views.LessonUpdateView.as_view(),
        name="lesson-update",
    ),
    path(
        "<slug:slug>/lesson/<int:pk>/delete/",
        views.LessonDeleteView.as_view(),
        name="lesson-delete",
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
