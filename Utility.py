import json

f = open('SpiritRecipies.json')

spirit_recipies = json.load(f)

def find_spirit_recipe(spirit:str) -> list:
    recipe_list = []
    for recipe in spirit_recipies:
        if recipe['Spirit'] == spirit:
            recipe_list.append(recipe)
    return recipe_list


# find_spirit_recipe('Aura Lion')