/*
Imagine you lean over and look at a cryptographer's notebook. You see some notes in the margin:
        4 + 9 = 1
        5 - 7 = 10
        2 + 3 = 5
At first you might think they've gone mad. Maybe this is why there are so many data leaks nowadays you'd think, but this is nothing more than modular arithmetic modulo 12 (albeit with some sloppy notation).

NB: in programming, % means mod (modulo)

You may not have been calling it modular arithmetic, but you've been doing these kinds of calculations since you learnt to tell the time (look again at those equations and think about adding hours).
Formally, "calculating time" is described by the theory of congruences. We say that two integers are congruent modulo m if a ≡ b mod m

Another way of saying this, is that when we divide the integer a by m, the remainder is b. This tells you that if m divides a (this can be written as m|a) then a ≡ 0 mod m.

To calculate 8146798528947 ≡ X mod 17, we start with current = 0. Then for each digit d in the number, we update current: current = (current * 10 + d) mod 17
At the end, current will hold the remainder X
NB: digits should be access from left to right
*/
#include <stdio.h>

long long moduloCalc(long long x, long long m);

int main(void){
    long long x, m;
    printf("to calculate the value of Y in (X ≡ Y mod m), Enter the value of X: ");
    scanf("%lld", &x);
    
    printf("Enter the value of m: ");
    scanf("%lld", &m);

    printf("%lld\n", moduloCalc(x, m));
    return 0;
}

long long moduloCalc(long long x, long long m){
    // This function calculates the value of Y in X ≡ Y mod m
    if (x == 0) return 0;
    
    long long current = 0;
    long long reversed = 0;
    long long temp = x;

    while (temp > 0){
        reversed = reversed * 10 + (temp % 10);
        temp /= 10;
    }

    while (reversed > 0){
        long long digit = reversed % 10;
        current = (current * 10 + digit) % m;
        reversed /= 10;
    }
    
    return current;
}