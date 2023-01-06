import wikipedia, os
os.system("cls")

stringy = "bicycle"

p = wikipedia.page(stringy, auto_suggest=False)

print(f"\nThere are {len(p.images)} bike images\n")

print(p.images)

