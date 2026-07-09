from django.urls import path,include
from .views import *
urlpatterns = [
    path('user_pay_courses/', OrdersView.as_view()),
    path('pay_callback/', PayCallBackView.as_view()),





]