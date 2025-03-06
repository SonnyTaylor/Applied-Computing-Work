def activity_1():
    """
	Create a dictionary that represents the details of a person with their name, age and city.
	Then write some code to do the following:
			• Print the dictionary
			• Update the age
			• Add their country to the dictionary
	"""
    person_details = {"name": "Joe Nutz", "age": 23, "city": "Melbourne"}

    print(person_details)
    person_details["age"] = 24
    person_details["country"] = "AU"

def activity_2():
    animals = {
		"lion": "mammal",
		"crocodile": "reptile",
		"sparrow": "bird",
		"trout": "fish",
		"komodo dragon": "reptile",
	}
	for animal, type in animals.items():
		if type == "reptile":
			print(animal)
   
