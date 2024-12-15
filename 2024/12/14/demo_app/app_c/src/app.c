#include <stdio.h>

int factorial(int num) {
    if (num == 1) {
        return num;
    }
    return num * factorial(num - 1);
}

int main(void)
{
    printf("=== App start ===\n");
    int num = 5;
    int result = factorial(num);
    printf("result: %d\n", result);
    printf("=== App end ===\n");
    return 0;
}
