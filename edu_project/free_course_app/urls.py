from django.urls import path,include
from .views import FreeCourseListView
urlpatterns = [
    path('free_courses/', FreeCourseListView.as_view()),
]