import	sys

kata = (2019, 9, 25, 3, 30)

def main( ):
    print("{1:0>2}/{2:0>2}/{0:0>4} {3:0>2}:{4:0>2}".format(*kata))

if __name__ == "__main__":
    main( )