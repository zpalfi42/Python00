import	sys

kata = (0, 4, 132.42222, 10000, 12345.67)

def main( ):
    print("module_{0:0>2}, ex_{1:0>2} : {2:.2f}, {3:.2e}, {4:.2e}".format(*kata))

if __name__ == "__main__":
    main( )