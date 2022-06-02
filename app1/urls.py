
from django.urls import path
from .views import our_team
urlpatterns = [
    path('', our_team, name='tenant'),
]
