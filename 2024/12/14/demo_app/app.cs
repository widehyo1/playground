using System;

namespace IntegralTypes
{
    class MainApp
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== App start ===");
            int num = 5;
            int result = factorial(num);
            Console.WriteLine($"result: {result}");
            Console.WriteLine("=== App end ===");
        }

        static int factorial(int num)
        {
            if (num == 1)
            {
                return num;
            }
            return num * factorial(num - 1);
        }
    }
}
