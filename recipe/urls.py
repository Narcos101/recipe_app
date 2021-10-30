from django.urls import path,include
from .views import recipes,recipe_details,recipe_add
urlpatterns = [
    path('',recipes,name="home"),
    path('add',recipe_add,name="add"),
    path('<recipe_id>',recipe_details),
]