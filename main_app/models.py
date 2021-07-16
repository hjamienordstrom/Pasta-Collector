from django.db import models
from django.urls import reverse

# Create your models here.

class Meat(models.Model):
    name = models.CharField(max_length=50)
    cut = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('meats_detail', kwargs={'pk': self.id})

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    pasta = models.CharField(max_length=100)
    sauce = models.CharField(max_length=100)
    vegetables = models.CharField(max_length=100)
    meats = models.ManyToManyField(Meat)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={ 'recipe_id', self.id })

class Instruction(models.Model):
    ingredients = models.CharField(max_length=100)
    directions = models.CharField(max_length=100)

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)