/*
In modular arithmetic, taking the square root of a number modulo a prime p means finding \
an integer a such that a ^ 2 ≡ x mod p. In other words, when a is squared and reduced modulo p, \
the result is x. If such an a exists, we say that x is a quadratic residue modulo p. Otherwise, \
x is a quadratic non-residue. For every quadratic residue, there are always two square roots: a \
and p - a, since both give the same result when squared modulo p. For example, with p = 29, \
if a = 11, then 11 ^ 2 mod 29 = 121 mod 29 = 5, so 11 is a square root of 5 modulo 29. \
Similarly, -11 and 18 are valid square root of 5 modulo 29. Quadratic residues only make up \
about half the elements in the set F_p^* (all integers from 1 to p - 1), and checking for \
them can be done by brute force when p is small.
*/

#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cstdint>


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

    
// Modular exponentiation: calculates (base^exp) mod mod
// Uses __uint128_t for safe multiplication to avoid overflow
uint64_t mod_exp(uint64_t base, uint64_t exp, uint64_t mod) {
    uint64_t result = 1 % mod;
    uint64_t current = base % mod;

    while (exp > 0) {
        if (exp & 1) {
            __uint128_t mul = (__uint128_t)result * current;
            result = static_cast<uint64_t>(mul % mod);
        }
        __uint128_t mul = (__uint128_t)current * current;
        current = static_cast<uint64_t>(mul % mod);
        exp >>= 1;
    }
    return result;
}

// Euler's Criterion: returns true if x is quadratic residue mod p, else false
bool is_quadratic_residue(uint64_t x, uint64_t p) {
    if (x == 0) return true; // 0 is always a residue
    uint64_t res = mod_exp(x, (p - 1) / 2, p);
    return res == 1;
}

// Find two square roots of x mod p assuming x is quadratic residue
// Returns true if roots found, false otherwise
bool find_square_roots(uint64_t x, uint64_t p, uint64_t& root1, uint64_t& root2) {
    for (uint64_t a = 0; a < p; a++) {
        __uint128_t sq = (__uint128_t)a * a;
        if (static_cast<uint64_t>(sq % p) == x % p) {
            root1 = a;
            root2 = (p - a) % p;
            return true;
        }
    }
    return false;
}

int main() {
    uint64_t p;
    std::string line;

    std::cout << "Enter prime modulus p: ";
    std::cin >> p;
    std::cin.ignore(); // consume newline

    std::cout << "Enter numbers separated by spaces: ";
    std::getline(std::cin, line);
    std::istringstream iss(line);

    std::vector<uint64_t> numbers;
    uint64_t val;
    while (iss >> val) {
        numbers.push_back(val);
    }

    std::cout << "Prime modulus: " << p << "\n\n";

    for (auto x : numbers) {
        std::cout << "Checking number: " << x << "\n";
        if (is_quadratic_residue(x, p)) {
            uint64_t r1, r2;
            if (find_square_roots(x, p, r1, r2)) {
                uint64_t smaller = (r1 < r2) ? r1 : r2;
                std::cout << "  Quadratic residue modulo " << p << "\n";
                std::cout << "  Square roots: " << r1 << " and " << r2 << "\n";
                std::cout << "  Smaller root (flag): " << smaller << "\n\n";
            } else {
                std::cout << "  Error: Could not find square roots for " << x << "\n\n";
            }
        } else {
            std::cout << "  Not a quadratic residue modulo " << p << "\n\n";
        }
    }

    return 0;
}
