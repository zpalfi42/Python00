import	sys

def main( args ):
	if (args.find(' ') != -1):
		print("AssertionError: more than one argument are provided")
	else:
		if (args.isdigit() == False):
			print("AssertionError: argument is not an integer")
		else:
			n = int(args)
			if (n % 2 != 0):
				print("I'm Odd.")
			else:
				print("I'm Even.")

if __name__ == "__main__":
    main( ' '.join(sys.argv[1:]) )