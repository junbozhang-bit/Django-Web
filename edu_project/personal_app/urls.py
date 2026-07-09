from django.urls import path,include
from .views import *
urlpatterns = [
    path('user_courses_name/', UserCourseNameListView.as_view()),
    path('user_courses_list/', UserCourseListView.as_view()),
    path('user_sections_list/', MySectionListView.as_view()),
    path('user_add_sections/', UserAddSectionView.as_view()),
    path('user_orders/', OrderListView.as_view()),




]