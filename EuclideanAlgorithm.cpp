/*
The Euclidean algorithm is a classic and efficient method for finding the greatest common divisor (GCD) of two long longegers.

Concept (How It Works)
Given two positive long longegers a and b:
1- Replace a with b, and b with a % b (the remainder).
2- Repeat step 1 until b == 0.
3- When b == 0, a is the GCD.

Greatest Common Divisor (GCD)

You can do it in 2 main ways in coding and here it is.
*/
#include <iostream>

long long gcd(long long a, long long b);

int main(){
    long long a, b;
    std::cout << "Enter number a: ";
    std::cin >> a;
    std::cout << "Enter number b: ";
    std::cin >> b;
    std::cout << gcd(a, b) << '\n';
}


long long gcd(long long a, long long b){
    if (b == 0){
        return a;
    }
    return gcd(b, a % b);
}