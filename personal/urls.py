from django.urls import path
from personal.views import home
urlpatterns = [
    path('', home, name='home'),
]
