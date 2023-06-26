from django.urls import path
from .views import *

urlpatterns = [
    path('graphic/', GraphicView.as_view(), name='graphic'),
]
