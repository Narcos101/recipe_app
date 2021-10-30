from django.contrib import admin
from .models import recipe


class recipeAdmin(admin.ModelAdmin):
    list_display = ('title','id')
    list_filter = ('timetaken',)


admin.site.register(recipe,recipeAdmin)