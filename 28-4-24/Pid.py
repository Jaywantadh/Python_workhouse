import os

def main():
    print("PID of running process : ",os.getpid())
    print("PID of parent process i.e command promt is : ",os.getppid())

if __name__ == "__main__":
    main()