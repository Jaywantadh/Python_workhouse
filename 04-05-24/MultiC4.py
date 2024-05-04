#Without multicore
import multiprocessing
import os
import time

def Fun(n):
   sum = 0
   print("PID is: ",os.getpid())
   for i in range(n):
      sum = sum + (n**3)

   return sum

def main():
    startTime = time.time()
    Arr = [1000,2000,3000,4000,5000,60000,70000,80000,90000,100000,110000,120000,130000,140000]
    result = []

    for value in Arr:
       result.append(Fun(value))

    print(result)
    endTime = time.time()
    print("Time required for execution:", endTime-startTime)
    
if __name__ == "__main__":
   main()