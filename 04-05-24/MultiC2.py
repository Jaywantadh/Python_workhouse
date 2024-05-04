import multiprocessing
import os

def Cube(n):
   print("PID is: ",os.getpid())
   return n**3

def main():
    Arr = [10,20,30,40,50]
    result = []

    p = multiprocessing.Pool()
    result = p.map(Cube,Arr)
    p.close()
    p.join()

    print(result)
    
if __name__ == "__main__":
   main()