'''
In modular arithmetic over a finite field, every non-zero element has a unique \
multiplicative inverse. This means that for any number g in the field Fp, there exists a number d such that g * d ≡ 1 mod p.

For example, to find the inverse of 3 modulo 13, we search for a number d that \
satisfies 3 * d ≡ 1 mod 13.
By testing values, we find that 3 * 9 = 27 ≡ 1 mod 13, \
so the inverse of 3 modulo 13 is 9. This inverse is important in cryptography  \
and number theory because it allows us to perform division in modular systems, \
which is otherwise not directly defined.

NB: if the GCD is not 1, then there is no multiplicative inverse.
'''

from EuclideanAlgorithm import GCDRecursive

def is_prime(n: int) -> bool:
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def modinv_euclid(a: int, m: int) -> int:
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 % m0

def modinv(a: int, m: int) -> int:
    if is_prime(m):
        return pow(a, m - 2, m)
    else:
        return modinv_euclid(a, m)

def main() -> None:
    a: int = int(input("to calculate the value of d in (a * d ≡ 1 mod m), Enter the value of a: "))
    m: int = int(input("Enter the value of m: "))
    if a == 0 or m <= 1:
        print("Invalid input. 'a' must be non-zero and 'm' > 1.")
        return
    if GCDRecursive(a, m) != 1:
        print("There is no Multiplicative Inverse (GCD ≠ 1).")
    else:
        print(f"The multiplicative inverse of {a} mod {m} is: {modinv(a, m)}")


if __name__ == '__main__':
    main()