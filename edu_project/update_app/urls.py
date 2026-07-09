from django.urls import path,include
from .views import *
urlpatterns = [
    path('update_courses/', UpdateCourseListView.as_view()),
    path('update_courses/<int:pk>/', UpdateCourseDetailView.as_view()),



]