from django.shortcuts import render

# Create your views here.
def recipes(request):
    api = [{'title':'Chicken kabab','description':'lorem ipsum','image':'https://img-global.cpcdn.com/recipes/53501194d626e345/400x400cq70/photo.jpg','id':'1'},{'title':'Chicken kabab','description':'lorem ipsum','image':'https://img-global.cpcdn.com/recipes/53501194d626e345/400x400cq70/photo.jpg','timetaken':'50minutes','id':'2'}]
    return render(request,'index.html',{'api':api})


def recipe_details(request,recipe_id):
    return render(request,'recipe_details.html')