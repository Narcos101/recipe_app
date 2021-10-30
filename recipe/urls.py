from django.urls import path,include
from .views import recipes,recipe_details,recipe_add
urlpatterns = [
    path('recipes/',recipes,name="home"),
    path('recipes/<recipe_id>',recipe_details),
    path('recipe',recipe_add,name="add"),
    path('success',success,name="success")
]