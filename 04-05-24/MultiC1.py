import os
def Cube(n):
   print("PID is: ",os.getpid())
   return n**3

def main():
    Arr = [10,20,30,40]
    result = []

    for Value in Arr:
       result.append(Cube(Value))

    print(result)
    
if __name__ == "__main__":
   main()