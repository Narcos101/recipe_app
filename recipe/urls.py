from django.urls import path,include
from .views import recipes
urlpatterns = [
    path('recipes/',recipes,name="home")
]