from django.urls import path,include
from .views import recipes
urlpatterns = [
    path('',recipes,name="home")
]