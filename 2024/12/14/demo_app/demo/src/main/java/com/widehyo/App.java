package com.widehyo;

/**
 * Hello world!
 */
public class App {
    public static void main(String[] args) {
        System.out.println("=== App start ===");
        int num = 5;
        int result = factorial(num);
        System.out.println("result: " + result);
        System.out.println("=== App end ===");
    }

    private static int factorial(int num) {
        if (num == 1) {
            return num;
        }
        return num * factorial(num - 1);
    }
}
