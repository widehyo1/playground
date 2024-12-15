#include <iostream>
using namespace std;

int factorial(int num) {
    if (num == 1) {
        return num;
    }
    return num * factorial(num - 1);
}

int main(void)
{
    cout << "=== App start ===" << endl;
    // int num = 5;
    int num = 8;
    int result = factorial(num);
    cout << "result: " << result << endl;
    cout << "=== App end ===" << endl;
    return 0;
}
