/*
In modular arithmetic over a finite field, every non-zero element has a unique \
multiplicative inverse. This means that for any number g in the field Fp, there exists a number d such that g * d ≡ 1 mod p.

For example, to find the inverse of 3 modulo 13, we search for a number d that \
satisfies 3 * d ≡ 1 mod 13.
By testing values, we find that 3 * 9 = 27 ≡ 1 mod 13, \
so the inverse of 3 modulo 13 is 9. This inverse is important in cryptography  \
and number theory because it allows us to perform division in modular systems, \
which is otherwise not directly defined.

NB: if the GCD is not 1, then there is no multiplicative inverse.
*/

#include <iostream>
#include <cstdint>
#include <limits>

uint64_t gcd(uint64_t a, uint64_t b);
uint64_t modinv(uint64_t a, uint64_t m);

int main(){
    uint64_t a, m;
    std::cout << "to calculate the value of d in (a * d ≡ 1 mod m), Enter the value of a: ";
    std::cin >> a;

    std::cout << "Enter the value of m: ";
    std::cin >> m;

    if (a == 0 && m <= 1){
        std::cout << "Invalid input. 'a' must be non-zero value and 'm' > 1." << std::endl;
        return 1;
    }
    if (gcd(a, m) != 1){
        std::cout << "There is no Multiplicative Inverse (GCD ≠ 1)." << std::endl;
        return 2;
    } else {
        printf("The multiplicative inverse of %llu mod %llu is: %llu", (unsigned long long)a, (unsigned long long)m, (unsigned long long)modinv(a, m));
    }
}

uint64_t gcd(uint64_t a, uint64_t b){
    if (b == 0){
        return a;
    }
    return gcd(b, a % b);
}

bool isPrime(uint64_t n){
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    uint64_t i = 5;
    while (i * i <= n){
        if (n % i == 0 || n % (i + 2) == 0) return false;
        i += 6;
    }
    return true;
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

uint64_t modinv_euclid(uint64_t a, uint64_t m){
    uint64_t m0, x0, x1;
    m0 = m;
    x0 = 0;
    x1 = 1;
    if (m == 1) return 0;

    uint64_t q;
    while (a > 1){
        q = a / m;
        uint64_t temp = m;
        m = a % m;
        a = temp;

        uint64_t tempX = x0;
        x0 = x1 - q * x0;
        x1 = tempX;
    }
    return x1 % m0;
}

uint64_t modinv(uint64_t a, uint64_t m){
    if (isPrime(m)) return mod_exp(a, m - 2, m);
    else return modinv_euclid(a, m);
}