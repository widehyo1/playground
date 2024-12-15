def factorial(num: int):
    if num <= 1:
        return num
    return num * factorial(num - 1)
    # return num * factorial(num - 2)

if __name__ == '__main__':
    print('=== App start ===')
    # num = 8
    num = 11
    result = factorial(num)
    print(f'result: {result}')
    print('=== App end ===')
