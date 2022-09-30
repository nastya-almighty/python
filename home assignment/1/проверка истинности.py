# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z

pred = [1, 0]

for x in pred:
    for y in pred:
        for z in pred:
            print (f"x = {x}, y = {y}, z = {z} {(not(x or y or z)) == ((not (x)) and (not (y)) and (not (z)))}")