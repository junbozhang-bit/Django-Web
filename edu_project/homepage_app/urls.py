from django.urls import path,include
from .views import *
urlpatterns = [
    path('rotation_charts/', RotationChartListView.as_view()),
    path('feature_services/', FeatureServiceListView.as_view()),

]