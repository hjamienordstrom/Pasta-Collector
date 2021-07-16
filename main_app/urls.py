from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('recipes/', views.recipes_index, name='index'),
    path('recipes/<int:recipe_id>/', views.recipes_detail, name='detail'),
    path('recipes/create/', views.RecipeCreate.as_view(), name='recipes_create'),
    path('recipes/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipes_update'),
    path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipes_delete'),
    path('recipes/<int:recipe_id>/add_instruction/', views.add_instruction, name='add_instruction'),
    path('recipes/<int:recipe_id>/assoc_meat/<int:meat_id>/', views.assoc_meat, name='assoc_meat'),
    path('meats/', views.MeatList.as_view(), name='meats_index'),
    path('meats/<int:pk>/', views.MeatDetail.as_view(), name='meats_detail'),
    path('meats/create/', views.MeatCreate.as_view(), name='meats_create'),
    path('meats/<int:pk>/update/', views.MeatUpdate.as_view(), name='meats_update'),
    path('meats/<int:pk>/delete/', views.MeatDelete.as_view(), name='meats_delete'),

]



