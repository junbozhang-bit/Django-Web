from django.urls import path,include
from .views import *
urlpatterns = [
    path('plans/', PlanDetailView.as_view()),
    path('class_types/', ClassTypeListView.as_view()),


]