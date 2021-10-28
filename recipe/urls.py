from django.urls import path,include
from .views import recipes,recipe_details
urlpatterns = [
    path('recipes/',recipes,name="home"),
    path('recipes/<recipe_id>',recipe_details)
]