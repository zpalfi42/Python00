import	sys

kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }

def main( ):
    print("Python was created by {}".format(kata.get("Python")))
    print("Ruby was created by {}".format(kata.get("Ruby")))
    print("PHP was created by {}".format(kata.get("PHP")))

if __name__ == "__main__":
    main( )