from django.shortcuts import render, redirect
from django.urls import reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def index(request):
    return redirect(reverse('recipe', kwargs={'dish': list(DATA.keys())[0]}))

def recipe(request, dish=''):
    recipe = {}
    servings = request.GET.get('servings', 1)
    if DATA.get(dish):
        for ingredient, amount in DATA.get(dish).items():
            recipe[ingredient] = round(amount * int(servings), 2)
    context = {
        'recipe': recipe,
    }
    return render(request, 'calculator/index.html', context)
