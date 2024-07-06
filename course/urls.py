from django.urls import path
from .views import (CoursesView, CourseDetailView, TeacherView, TeacherDetailView,
                    StudentView, StudentDetailView)

urlpatterns = [
    path('api/v1/', CoursesView.as_view()),
    path('api/v1/<int:pk>/', CourseDetailView.as_view()),
    path('api/v2/', TeacherView.as_view()),
    path('api/v2/<int:pk>/', TeacherDetailView.as_view()),
    path('api/v3/', StudentView.as_view()),
    path('api/v3/<int:pk>/', StudentDetailView.as_view()),
]