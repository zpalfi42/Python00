import	sys

def main( args ):
    if (len(args) is 1):
        print("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
        return 
    
    if (len(args) is not 3):
        print("AssertionError: invlaid number of arguments")
        return
    
    if (args[1].isdigit() is not True or args[2].isdigit() is not True):
        print("AssertionError: only integers")
        return
    
    num1 = int(args[1])
    num2 = int(args[2])
    
    print("Sum:\t\t" + str(num1 + num2))
    print("Difference:\t" + str(num1 - num2))
    print("Product:\t" + str(num1 * num2))
    if (num2 is not 0):
        print("Quotient:\t" + str(float(num1) / float(num2)))
    else:
        print("Quotient:\tERROR (division by zero)")
    
    if (num2 is not 0):
        print("Reminder:\t" + str(num1 % num2))
    else:
        print("Quotient:\tERROR (division by zero)")

if __name__ == "__main__":
    main( sys.argv )