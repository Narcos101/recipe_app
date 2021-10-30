from django.shortcuts import render
from .models import recipe
from .forms import Recipeform

def recipes(request):
    api = recipe.objects.all()
    return render(request,'index.html',{'api':api})


def recipe_details(request,recipe_id):
    try:
        selected_recipe = recipe.objects.get(id=recipe_id)
        return render(request,'recipe_details.html',{'selected_recipe':selected_recipe})
    except:
        return render(request,'404.html')

def recipe_add(request):
    if request.method == 'GET':
        form = Recipeform()
        return render(request,'recipe_add.html',{'form':form})
    else:
        form = Recipeform(request.POST,request.FILES)
        print(form.data)
        if form.is_valid():
            form.save()
        return render(request,'success.html')
    