def cakes(recipe, available):
    product = []
    for key in recipe:
        if key in available:
            product.append(int(available[key] / recipe[key]))
        else:
            return 0
    product.sort()
    return product[0]


def cakes(recipe, available):
    return min(available.get(k, 0)/recipe[k] for k in recipe)

def cakes(recipe, available):
    try:
        return min([available[a]/recipe[a] for a in recipe])
    except:
        return 0

def cakes(recipe, available):
    return min(available.get(k, 0) // v for k,v in recipe.iteritems())

def cakes(recipe, available):
    ''' Take each ingredient from the recipe, see if it is in the available ones
        and calculate how many full cakes you can make with it.
        If an ingredient is missing, we can't bake a cake. Otherwise we have to
        find the lowest possible amount of cakes.'''
    return min([available[i]//recipe[i] if i in available else 0 for i in recipe])

def cakes(recipe, available):
    list = []
    for ingredient in recipe:
        if ingredient in available:
            list.append(available[ingredient]/recipe[ingredient])
        else:
            return 0
    return min(list)

def cakes(recipe, ingredients):
    return min(ingredients.get(k, 0) / v for k, v in recipe.iteritems())

def cakes(recipe, available):
    return min((available.get(k, 0) // v for k, v in recipe.items()))
