def cakes(recipe, available):
    product = []
    for key in recipe:
        if key in available:
            product.append(int(available[key] / recipe[key]))
        else:
            return 0
    product.sort()
    return product[0]



