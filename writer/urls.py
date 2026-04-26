from django.urls import path
from .views import home, history, index

urlpatterns = [
    path('', index, name='index'),
    path('history/', history, name='history'),
    path('generate-post/', home, name='generate-post'),
]