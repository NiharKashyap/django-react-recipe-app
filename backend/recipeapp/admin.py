import imp
from django.contrib import admin
from .models import RecipeModel
# Register your models here.


class RecipeAdmin(admin.ModelAdmin):
    pass

admin.site.register(RecipeModel,RecipeAdmin)
