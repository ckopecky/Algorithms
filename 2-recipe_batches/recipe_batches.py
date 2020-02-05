#!/usr/bin/python

import math

'''
recipe = {} 
  form = "ingredient_name: int amount needed"
ingredients = {}
  form = "ingredient_name: int amount have"

the problem here is that we have some ingredients and we have a recipe. We want to find out if we can make the given recipe using the ingredients we have. If we can, we want to find out how many batches of the recipe we can make. 

First thing we should do is loop through the recipe to see if that ingredient is in our stash...if not, we don't have the ingredients available to make the dish.

In the same loop we should check the amounts. If what we have is less than what the recipe calls for, then we don't have the ingredients available to make the dish.

If it passes these two checks:

we need some sort of tracker that tracks the minimum number of batches each ingredient can make. 

so if we loop through the what we have list, we take the same property in the recipe list, and divide/floor what we have to what is needed. That will be the initial maximum number of batches we can make. 

When we get to next ingredient, we run through same process, but if the num of batches is lower than the current, we reassign max number of batches. 

return max number of batches


'''

def recipe_batches(recipe, ingredients):
  max_batches = float('inf')
  for ingredient in recipe: 
    if ingredient not in ingredients:
      return 0
    elif ingredients[ingredient] < recipe[ingredient]:
      return 0
    
    else:
      num_batches = ingredients[ingredient]//recipe[ingredient]
      if max_batches >= num_batches:
        max_batches = num_batches


  return max_batches 




if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'cheese': 10 }
  ingredients = { 'milk': 198, 'butter': 52, 'cheese': 10 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))