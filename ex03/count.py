import	sys

def	text_analyzer( s=None ):
    ''' This function counts the number of upper characters, lower characters, punctuation and spaces in a given text. '''
    l = "abcdefghijklmnopqrstuvwxyz"
    u = l.upper()
    p = ",.;'-?!"
    sp = " "
    if (s is None):
        s = input("What is the text to analyze?\n>> ")
    
    if (type(s) is not str):
        print("Error")
    else:   
        print("The text contains " + str(len(s)) + " character(s):\n")
        cl = cu = cp = csp = 0
        for i in s:
            if (i in l):
                cl += 1
                
            if (i in u):
                cu += 1
                
            if (i in p):
                cp += 1
                
            if (i in sp):
                csp += 1
                
            if (i not in l and i not in u and i not in p and i not in sp):
                print("------->" + i)
        
        print("- " + str(cu) + " upper letter(s)\n")
        print("- " + str(cl) + " lower letter(s)\n")
        print("- " + str(cp) + " punctuation mark(s)\n")
        print("- " + str(csp) + " space(s)\n")

def main( args ):
    if (1 < len(args) < 3):
        text_analyzer(args[1])
    else:
        print("Error: Invalid arguments!")

if __name__ == "__main__":
    main( sys.argv )
    