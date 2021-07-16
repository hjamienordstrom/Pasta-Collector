from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Recipe, Meat
from .forms import InstructionForm
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def recipes_index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', {'recipes': recipes })

def recipes_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    meats_recipe_doesnt_have = Meat.objects.exclude(id__in = recipe.meats.all().values_list('id'))
    instruction_form = InstructionForm
    return render(request, 'recipes/detail.html', {
      'recipe' : recipe , 'instruction_form':instruction_form,
      'meats' : meats_recipe_doesnt_have
    })

class RecipeCreate(CreateView):
    model = Recipe
    fields = '__all__'
    success_url = '/recipes/'

class RecipeUpdate(UpdateView):
  model = Recipe
  fields = ['pasta','sauce','vegetables']
  success_url = '/recipes/'

class RecipeDelete(DeleteView):
  model = Recipe
  success_url = '/recipes/'

def add_instruction(request,recipe_id):
  form = InstructionForm(request.POST)
  if form.is_valid():
    new_instruction = form.save(commit=False)
    new_instruction.recipe_id = recipe_id
    new_instruction.save()
  return redirect('detail', recipe_id=recipe_id)
  
class MeatList(ListView):
  model = Meat

class MeatDetail(DetailView):
  model = Meat

class MeatCreate(CreateView):
  model = Meat
  fields = '__all__'

class MeatUpdate(UpdateView):
  model = Meat
  fields = '__all__'

class MeatDelete(DeleteView):
  model = Meat
  success_url = '/meats/'

def assoc_meat(request, recipe_id, meat_id):
  Recipe.objects.get(id=recipe_id).meats.add(meat_id)
  return redirect('detail', recipe_id=recipe_id)