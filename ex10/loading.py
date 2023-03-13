import	sys
import  time

start = time.time()

N = 3333

def ft_progress( lst ):
    prev = time.time()
    new = prev
    for i in lst:
        if (i is 1):
            new = time.time()
        yield i
        print("ETA: {:.2f}s [{:>3}%][{:<11}] {:>3}/{} | elapsed time {:>3.2f}s".format((new - prev) * (len(lst)), int((i/len(lst))*100), "="*int(((i+1)/len(lst))*10)+">", i, len(lst) - 1, time.time() - start), end="\r")

def main( args ):
    listy= range(N)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
        time.sleep(0.005)
    print()
    print(ret)

if __name__ == "__main__":
    main( sys.argv )