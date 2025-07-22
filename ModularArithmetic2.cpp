/*
Understanding Modular Arithmetic and Fermat's Little Theorem
-------------------------------------------------------------

When working with integers modulo a number p, the structure of \
the resulting set depends on whether p is prime or not. If p is\
a prime number, the integers modulo p form a mathematical struc-
ture known as a *finite field*, denoted by Fₚ. In this field,  \
every nonzero element has a unique multiplicative inverse, and \
the set supports both addition and multiplication operations wi-
th identity elements (0 for addition, 1 for multiplication).

If p is not a prime number, the integers modulo p form a *ring*,\
which still supports addition and multiplication, but not every \
element has a multiplicative inverse.

In the context of a finite field Fₚ where p is prime, Fermat's \
Little Theorem becomes a fundamental tool. It states:

    If p is a prime number and a is an integer not divisible by p, then:
    a ^ (p - 1) ≡ 1 mod p

This means that raising a number to the (p - 1)th power modulo \
p yields 1. This result has several important consequences, inc-
luding an efficient way to compute modular inverses:

    a ^ (-1) ≡ a ^ (p - 2) mod p

This is especially useful in number theory and cryptography.

To illustrate, consider p = 17. Then F₁₇ = {0, 1, 2, ..., 16}. Let's evaluate the following:

    3^17 mod 17
    5^17 mod 17
    7^16 mod 17

By Fermat’s theorem:
    3^17 ≡ 3 mod 17 (since 3^17 = 3 * 3^16 ≡ 3 * 1 mod 17)
    5^17 ≡ 5 mod 17
    7^16 ≡ 1 mod 17

This confirms the theorem’s validity for these cases.

Now consider a much larger prime: p = 65537. This number is a \
Fermat prime and is frequently used in RSA cryptography due to\
its efficient properties. Let's compute the following:

    (27324678765)^4 mod 65537 = x
    x^65536 mod 65537

Because 65537 is prime, and Fermat's theorem tells us that for any a ≠ 0 mod 65537, we have:

    a^65536 ≡ 1 mod 65537

Therefore, the result of x^65536 mod 65537 will be 1, assuming x is not divisible by 65537.

This demonstrates how Fermat’s Little Theorem allows us to evaluate \
complex modular exponentiation quickly and accurately, which is esse-
ntial for the efficiency of public-key cryptographic systems like RSA.

BY ChatGPT
*/

#include <iostream>
#include <cstdint>
#include <limits>

uint64_t mod_multi(uint64_t a, uint64_t b, uint64_t mod);
uint64_t mod_exp(uint64_t base, uint64_t exponent, uint64_t modulus);

int main(){
    std::cout << "Modular Exponentiation Calculator\n";
    std::cout << "This computes: (base ^ exponent) mod modulus\n";

    uint64_t base, exponent, modulus;

    std::cout << "Enter base:\t";
    while (!(std::cin >> base)){
        std::cout << "Invalid input. Enter a non-negative integer for base: ";
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    }

    std::cout << "Enter exponent:\t";
    while(!(std::cin >> exponent)){
        std::cout << "Invalid input. Enter a non-negative integer for base: ";
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    }

    std::cout << "Enter modulus:\t";
    while(!(std::cin >> modulus)){
        std::cout << "Invalid input. Enter a non-negative integer for base: ";
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    }

    if (modulus <= 0){
        printf("Modulus must be a positive integer.");
        return 0;
    }

    uint64_t result = mod_exp(base, exponent, modulus);
    printf("\nResult: (%llu ^ %llu) mod %llu = %llu\n", (unsigned long long)base, (unsigned long long)exponent, (unsigned long long)modulus, (unsigned long long)result);

    return 0;
}

uint64_t mod_multi(uint64_t a, uint64_t b, uint64_t mod){
    /*
    * NOTE:
    * This code uses `__uint128_t` for 128-bit multiplication to ensure correctness with large numbers,
    * especially in cryptographic applications like RSA. This type is supported by GCC on Linux but 
    * NOT on MinGW (Windows GCC). 
    *
    * You can **replace `__uint128_t` with `uint64_t`**, but you're **GAMBLING with correctness**
    * for large values — overflow may happen silently.
    *
    * RECOMMENDED SOLUTIONS if `__uint128_t` fails:
    *   - Use **WSL** (Windows Subsystem for Linux)
    *   - Compile on a **Linux** machine or VM
    *   - Use **GMP** library for big integer support (preferred for professional-grade cryptography)
    *
    * Never compromise precision in cryptographic applications.
    */
    __uint128_t result = (__uint128_t) a * b;
    return (uint64_t)(result % mod);
}

uint64_t mod_exp(uint64_t base, uint64_t exponent, uint64_t modulus){
    uint64_t result = 1;
    base %= modulus;

    while (exponent > 0) {
        if (exponent & 1) {
            result = mod_multi(result, base, modulus);
        }
        base = mod_multi(base, base, modulus);
        exponent >>= 1;
    }
    return result;
}