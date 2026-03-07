import os
import sys
from functools import wraps

def main():
    cell = ('.', 'C', '/', '\\')
    direction = ('U', 'R', 'D', 'L')
    
    N, M = [int(char) for char in input().split()]
    for _ in range(N):
        print("===")
        for c in input():
            print(c)

if os.getenv("DEBUG"):
    from utils import dump_runtime_environment
    main = dump_runtime_environment(main)

if __name__ == "__main__":
    main()
