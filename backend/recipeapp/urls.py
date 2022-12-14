from django.urls import path, include
from .views import RecipeView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'recipe', RecipeView)
urlpatterns = router.urls