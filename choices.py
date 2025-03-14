import random

mylist = ["falla", "+1daño", "golpe_mortal"]

print(random.choices(mylist, weights=[50, 49, 1], k=100))
