package com.widehyo;

import java.util.List;

public class App {
    public static void main( String[] args ) {
        System.out.println("* App start ====================");
        int result = factorial(5);
        System.out.println("result: " + result);
        System.out.println("* App end ======================");
        System.out.println();
    }

    private static int factorial(int number) {
        if (number == 1) {
            return number;
        }
        return number * factorial(number - 1);
    }

}
