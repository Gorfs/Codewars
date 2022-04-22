
def cakes(recipe, available):
    counts_arr = []
    count = 0
    for item in recipe:
        if item not in available or available[item] < recipe[item]:
            return 0
        if recipe[item] <= available[item]:
            count = available[item]//recipe[item]
            counts_arr.append(count)
        count = 0
    return min(counts_arr)
        
    

print(cakes({'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100},{'sugar': 500, 'flour': 2000, 'milk': 2000, 'apples': 15, 'oil': 20}))