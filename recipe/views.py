from django.shortcuts import render
from .models import recipe

# Create your views here.
def recipes(request):
    api = recipe.objects.all()
    return render(request,'index.html',{'api':api})


def recipe_details(request,recipe_id):
    try:
        selected_recipe = recipe.objects.get(id=recipe_id)
        return render(request,'recipe_details.html',{'selected_recipe':selected_recipe})
    except:
        return render(request,'404.html')