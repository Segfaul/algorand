from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),

    path('', PlotAlgorithmPerformanceView.as_view(), name='plot_algorithm_performance'),
    path('find_value/', ArraySearchView.as_view(), name='array_search'),
]
