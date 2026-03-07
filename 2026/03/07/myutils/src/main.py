import os

def main():
    N = int(input())
    numbers = [int(num) for num in input().split()]
    target = int(input())
    # 1 / 0
    print(sum(1 for num in numbers if num == target))

if os.getenv("DEBUG"):
    from utils import dump_runtime_environment, ex_hook
    import sys
    main = dump_runtime_environment(main)
    sys.excepthook = ex_hook

if __name__ == "__main__":
    main()
