from django.urls import path,include
from .views import TeacherListView
urlpatterns = [
    path('teachers/', TeacherListView.as_view()),
]