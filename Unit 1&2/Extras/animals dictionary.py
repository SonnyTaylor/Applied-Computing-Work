# For the dictionary in the screenshot bellow write some code that iterates through the dictionary and prints animal name where the animal is a reptile.

animals = {
    "lion": "mammal",
    "crocodile": "reptile",
    "sparrow": "bird",
    "trout": "fish",
    "komodo dragon": "reptile",
}

for i in animals:
    print(f"{i} is a {animals[i]}")
