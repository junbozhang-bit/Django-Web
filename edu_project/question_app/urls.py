from django.urls import path,include
from .views import *
urlpatterns = [
    path('user_questions/', QuestionView.as_view()),
    path('user_answers/', AnswerView.as_view()),
    path('get_questions/', QuestionListView.as_view()),
    path('get_questions/<int:pk>/', QuestionDetailView.as_view()),
    path('question_sections/', QuestionSectionListView.as_view()),








]