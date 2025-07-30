'''
In number theory and cryptography, you often need to find the square root of a number modulo a prime. That is, given integers a and prime p, you want to find an integer r such that:
        r² ≡ a mod p

This is called finding a **modular square root**. For example if p = 13 and a = 10, one such solution is r = 6, because 6² = 36 ≡ 10 mod 13. But doing this for massive primesm like 2048-but ones used in crypto is not something you can brute-force. That's where Tonelli-Shanks comes in.


WHY IS THIS IMPORTANT IN CYBERSECURITY?
Modular square roots are fundamental in Elliptic Curve Cryptography (ECC). Points on an elliptic curve are defined by an equation like:
        y² ≡ (x³ + ax + b) mod p

To find a point (x, y) on the curve, you must solve this equation for y, given x. That means taking the square root modulo a large prime p, exactly what Tonelli-Shanks does efficiently.
This operation is used during key generation, encryption, digital signatures, and many cryptographic protocols (like ECDSA, Diffie-Hellman, etc.).


THEORETICAL BACKGROUND
1. Legendre Symbol
-------------------
To even ask if a square root exists, we need a quick test. The Legendre symbol tells us whether 
a number `a` is a quadratic residue modulo a prime `p`—in other words, whether a solution to:

    r² ≡ a mod p

exists.

It is defined as:

    (a | p) = {
        1  if a is a quadratic residue mod p,
       -1  if a is not a quadratic residue mod p,
        0  if a ≡ 0 mod p
    }

We can compute this efficiently using Euler's criterion:

    (a | p) ≡ a^((p - 1) // 2) mod p

If the result is 1, a square root exists. If not, we stop.

2. Special Case: p ≡ 3 mod 4
-----------------------------
If the prime `p` satisfies:

    p ≡ 3 mod 4

There's a shortcut to compute the square root:

    r ≡ a^((p + 1) // 4) mod p

This is derived from Fermat's Little Theorem and is very efficient. However, it doesn't work 
for the more common case where:

    p ≡ 1 mod 4

In that case, we need a more general method.

Tonelli-Shanks Algorithm (General Case)
-------------------------------------------
When p ≡ 1 mod 4, Tonelli-Shanks provides a powerful and general solution to finding modular square roots.

Step-by-step process:

1. Check if a solution exists using the Legendre symbol.
2. Factor p - 1 as:  p - 1 = q * 2^s   where q is odd.
3. Find a non-quadratic-residue z (i.e., a number such that (z | p) = -1).
4. Set up:
    - r: current guess for the root
    - t: the current “error” value (a^q mod p)
    - c: powers of the non-residue (z^q mod p)
    - m: exponent that tracks powers of 2
5. Loop until t = 1:
    - Find the smallest i such that t^(2^i) ≡ 1 mod p
    - Update r, t, c, and m accordingly
6. Return the smaller of the two roots (r or p - r), since every quadratic residue a mod p has two roots.

The Tonelli-Shanks algorithm runs in O(log^2 p) time and is efficient even with large 2048-bit primes.
'''

def legendre_symbol(a, p):
    return pow(a, (p - 1) // 2, p)

def tonelli_shanks(a, p):
    if legendre_symbol(a, p) != 1:
        return None

    if p % 4 == 3:
        return pow(a, (p + 1) // 4, p)

    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1

    z = 2
    while legendre_symbol(z, p) != p - 1:
        z += 1

    m = s
    c = pow(z, q, p)
    t = pow(a, q, p)
    r = pow(a, (q + 1) // 2, p)

    while t != 1:
        i, temp = 0, t
        while temp != 1:
            temp = pow(temp, 2, p)
            i += 1
            if i == m:
                return None

        b = pow(c, 2 ** (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i

    return min(r, p - r)

def load_input(filename):
    a = None
    p = None

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("a ="):
                a = int(line.split("=")[1].strip())
            elif line.startswith("p ="):
                p = int(line.split("=")[1].strip())
    
    if a is None or p is None:
        raise ValueError("Could not find 'a' or 'p' in the input file")
    return a, p


def main():
    input_file = r"input.txt"
    a, p = load_input(input_file)
    root = tonelli_shanks(a, p)
    if root is None:
        print("No square root exists for a modulo p.")
    else:
        print("Square root:", root)

if __name__ == "__main__":
    main()