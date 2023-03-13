import	sys

result = []
p = ",.;'-?!"

def main( args ):
    if (len(args) is not 3):
        print("ERROR")
        return
    if (args[2].isdigit() is False):
        print("EROOR")
        return
        
    cleaned = str(args[1])
    for i in p:   
        cleaned = cleaned.replace(i, "")
    words = cleaned.split(" ")
    n = int(args[2])
    for i in words:
        if (len(i) > n):
            result.append(i)
    print(result)
            

if __name__ == "__main__":
    main( sys.argv )