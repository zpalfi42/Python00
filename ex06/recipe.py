import	sys

cookbook = {
        "bocadillo" : {
            "ingredients" : {
                "jamon",
                "pan",
                "queso",
                "tomate"
            },
            "meal" : "almuerzo",
            "prep_time" : 10
        },
        "tarta" : {
            "ingredients" : {
                "harina",
                "huevos",
                "azucar"
            },
            "meal" : "postre",
            "prep_time" : 60
        },
        "ensalada" : {
            "ingredients" : {
                "aguacate",
                "rucula",
                "tomate",
                "espinacas"
            },
            "meal" : "almuerzo",
            "prep_time" : 15
        }
    }

def recipe_details( recipe ):
    print(cookbook.get(recipe))

def recipe_names( ):
    print(cookbook.keys())
    
def recipe_delete( recipe ):
    if (recipe in cookbook.keys()):
        cookbook.pop(recipe)
        
def recipe_add( ):
    name = input(">>> Enter a name:\n")
    while (True):
        if (name in cookbook.keys()):
            name = input(">>> Recipe name alredy in use, please enter a valid name:\n")
        else:
            break
    print("\n>>> Enter ingredients:")
    ingredients = []
    while (True):
        ingredient = input()
        if (len(ingredient) is 0):
            break
        ingredients += ingredient
        
    meal = input(">>> Enter a meal type:\n")
    while(True):
        if (len(meal) is not 0):
            break
        else:
            meal = input(">>> Enter a meal type:\n")

    prep_time = input("\n>>> Enter a preparation time:\n")
    while(True):
        if (len(prep_time) is not 0 and prep_time.isdigit() is True):
            break
        else:
            prep_time = input(">>> Enter a preparation time:\n")
    
    aux = {
        name : {
            "ingredients" : ingredients,
            "meal" : meal,
            "prep_time" : prep_time
        }
    }
    
    cookbook.update(aux)

def print_info():
    print("List of available option:")
    print("\t1: Add a recipe")
    print("\t2: Delete a recipe")
    print("\t3: Print a recipe")
    print("\t4: Print the cookbook")
    print("\t5: Quit")
    

def main( args ):
    print("Welcome to the Python Cookbook !")
    print_info()
    
    while (True):
        i = input("\nPlease select an option:\n>> ")
        if i is "1":
            recipe_add()
            continue
        if i is "2":
            recipe = input("\nPlease enter a recipe name to delete:\n>> ")
            recipe_delete(recipe)
            continue
        if i is "3":
            recipe = input("\nPlease enter a recipe name to get its details:\n>> ")
            recipe_details(recipe)
            continue
        if i is "4":
            recipe_names()
            continue
        if i is "5":
            print("\nCookbook closed. Goodbye !")
            break
        else:
            print("Sorry, this option does not exist.")
            print_info()

if __name__ == "__main__":
    main( sys.argv )