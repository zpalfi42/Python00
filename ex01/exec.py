import	sys

def main( args ):
	print(args.swapcase()[::-1])

if __name__ == "__main__":
    main( ' '.join(sys.argv[1:]) )