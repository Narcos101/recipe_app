from django.shortcuts import render

# Create your views here.
def recipes(request):
    api = [{'title':'Chicken kabab','description':'lorem ipsum','image':'https://img-global.cpcdn.com/recipes/53501194d626e345/400x400cq70/photo.jpg'},{'title':'Chicken kabab','description':'lorem ipsum','image':'https://img-global.cpcdn.com/recipes/53501194d626e345/400x400cq70/photo.jpg','timetaken':'50minutes'}]
    return render(request,'index.html',{'api':api})


def recipe_details(request):
    return render(request,'recipe_details.html')