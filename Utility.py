import json
from Resources import make_spirit_recipes_json

try:
    f = open('SpiritRecipies.json')
except FileNotFoundError:
    make_spirit_recipes_json()
    f = open('SpiritRecipies.json')

spirit_recipies = json.load(f)

def find_spirit_recipe(spirit:str) -> list:
    print(f"find_spirit_recipe: searching for {spirit}")
    recipe_list = []
    for recipe in spirit_recipies:
        print(f"find_spirit_recipe: checking {recipe['Spirit']}")
        if recipe['Spirit'] == spirit:
            print(f"find_spirit_recipe: found {spirit}")
            recipe_list.append(recipe)
    print(f"find_spirit_recipe: returning {recipe_list}")
    return recipe_list


# find_spirit_recipe('Aura Lion')