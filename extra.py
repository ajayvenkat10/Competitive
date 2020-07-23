import json
import requests
from bs4 import BeautifulSoup
from random import randint
from time import sleep


def convert_time_to_minutes(time):
    time_parts = time.split()
    time_in_minutes = float(time_parts[0])
    if (time_parts[-1].lower() == "day"):
        time_in_minutes = time_in_minutes * 24 * 60
    if (time_parts[-1].lower() == "hour" or time_parts[-1].lower() == "hours"
            or time_parts[-1].lower() == "hr"
            or time_parts[-1].lower() == "hrs"):
        time_in_minutes = time_in_minutes * 60

    return time_in_minutes


def strip_units(recipe):
    if (recipe["calories"]):
        calories_parts = recipe["calories"].split()
        recipe["calories"] = float(calories_parts[0])

    if (recipe["servings"]):
        servings_parts = recipe["servings"].split()
        for elements in servings_parts:
            if (elements.isnumeric()):
                recipe["servings"] = int(elements)
                break
    if (recipe["preparationTimeInMinutes"]):
        recipe["preparationTimeInMinutes"] = convert_time_to_minutes(
            recipe["preparationTimeInMinutes"])

    if (recipe["cookingTimeInMinutes"]):
        recipe["cookingTimeInMinutes"] = convert_time_to_minutes(
            recipe["cookingTimeInMinutes"])

    return recipe


def get_tags(soup):
    tags = []
    for tag_element in soup.find_all('', itemprop="recipeCategory"):
        tags.append(tag_element.text)
    return tags


def get_directions(soup):
    instructions = soup.find('', itemprop="recipeInstructions")
    directions = []
    for instruction in instructions.find_all('', itemprop="itemListElement"):
        directions.append(instruction.text)
    return directions


def get_ingredients(soup):
    ingredients = []
    contains_egg = False
    for ingredient_element in soup.find_all('', itemprop='recipeIngredient'):
        measurement = ingredient_element.span.text
        ingredient = {}
        if (len(measurement) > 0):
            measurement_parts = measurement.split(' ')
            if (measurement_parts[-1].isalpha()):
                ingredient["unit"] = measurement_parts[-1]
                measurement_parts = measurement_parts[:-1]
            ingredient["amount"] = " ".join(measurement_parts)

        ingredient["name"] = ingredient_element.a.span.text
        ingredient["url"] = ingredient_element.a.get("href")
        contains_egg = contains_egg or ("egg" in ingredient["name"].lower())

        ingredients.append(ingredient)

    return ingredients, contains_egg


def extract_recipe(url, course_type):
    page = requests.get(url)
    # Create a BeautifulSoup object
    soup = BeautifulSoup(page.text, 'lxml')
    selectors = {
        "name": "name",
        "description": "description",
        "calories": "calories",
        "cookingTimeInMinutes": "cookTime",
        "preparationTimeInMinutes": "prepTime",
        "servings": "recipeYield",
    }
    recipe = {"vegetarian": True, "courseType": [course_type], "url": url}

    soup = soup.find("div", id="recipesubpanel")
    for key in selectors.keys():
        element = soup.find('', itemprop=selectors[key])
        if (element != None):
            recipe[key] = element.text
        else:
            recipe[key] = None

    recipe["directions"] = get_directions(soup)
    recipe["ingredients"], recipe["containsEgg"] = get_ingredients(soup)
    recipe["tags"] = get_tags(soup)
    recipe = strip_units(recipe)
    return recipe


# recipe = extract_recipe(
# 'https://www.tarladalal.com/Hara-Bhara-Kebab-(-Kebabs-and-Tikkis-Recipes)-32747r'
# )

base_url = "https://www.tarladalal.com/"


def recipes(url, course_type):
    page_index = 1
    while (True):
        url += "?pageindex=" + str(page_index)
        print(url)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'lxml')
        recipes = []
        recipe_list = soup.find("div", class_="recipelist")
        if (recipe_list == None or page_index == 2):
            break
        for recipe_url in recipe_list.find_all('', itemprop="url"):
            recipe = extract_recipe(base_url + recipe_url.get("href"),
                                    course_type)
            recipes.append(recipe)
            sleep(randint(100, 1000) / 1000.0)
        page_index += 1

    return recipes


print(
    json.dumps(
        recipes(
            "https://www.tarladalal.com/recipes-for-breakfast--Indian-veg-breakfast-recipes-151",
            "breakfast")))
