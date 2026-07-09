from django.urls import path,include
from .views import *
urlpatterns = [
    path('courses/', CourseListView.as_view()),
    path('stages/', StageListView.as_view()),
    path('chapters/', ChapterListView.as_view()),
    path('sections/', SectionListView.as_view()),
    path('stages/<int:pk>/', StageDetailView.as_view()),


]