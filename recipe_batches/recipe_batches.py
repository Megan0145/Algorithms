#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # 1: make sure we have all ingredients, regardless of quantity
  # ie. if recipe dictionary has key 'cheese' and ingredients doesn't, return 0
  if recipe.keys() != ingredients.keys():
    return 0
  
  # 2: for every ingredient in the recipe (for every key in recipe dict), 
  # divide the quantity we have of that ingredient by the quantity needed in the recipe
  # eg. key 'milk' in recipe dict has value of 100 and key 'milk' in ingredients dict has value of 200 ->
  #     200 // 100 = 2 (using floor division operator '//' to round down)
  # save result in 'max_batches' list containing max number of batches that can be made for each ingredient
  max_batches = []
  
  for ing in recipe:
    max_batches.append(ingredients[ing] // recipe[ing])
  
  # 3: return the minimum value in the max_batches array
  # (if the maximum no of batches we could make with the milk we have is 500 but the maximum no. of batches we could 
  # make with the butter we have is only 10, we're still only going to be able to make 10 batches)
  return min(max_batches)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))