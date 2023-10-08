from django.urls import path
from .views import *

urlpatterns = [
    path("", Schools.as_view()),
    path("number/<int:num>/", number),
    path("number/", number)
]