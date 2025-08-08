"""
Chinese Remainder Theorem (CRT)

In number theory, the Chinese Remainder Theorem gives a unique solution to a system of linear congruences when the moduli are pairwise coprime.

That is, given:
    x ≡ a₁ mod n₁  
    x ≡ a₂ mod n₂  
    ...  
    x ≡ a_k mod n_k

If all nᵢ are pairwise coprime, then there exists a unique solution modulo N = n₁ * n₂ * ... * n_k.

--------------------------
WHY IS THIS IMPORTANT IN CRYPTOGRAPHY?

CRT allows us to split large integer problems into smaller ones. This is especially helpful in speeding up RSA decryption using the Chinese Remainder Theorem optimization, where modular exponentiation is done modulo p and q (RSA primes) instead of n = p*q.

--------------------------
THEORETICAL BACKGROUND

Let:
    x ≡ a₁ mod n₁  
    x ≡ a₂ mod n₂  
    ...
    x ≡ a_k mod n_k  

1. Compute N = n₁ * n₂ * ... * n_k
2. For each i:
    - Let Nᵢ = N // nᵢ
    - Let mᵢ = modular inverse of Nᵢ mod nᵢ
3. Final solution:
    x ≡ Σ (aᵢ * Nᵢ * mᵢ) mod N

The result x is the unique integer modulo N that satisfies all the congruences.
"""

from ExtendedGCD import extendedGCD

def modinv(a, m):
    g, x, _ = extendedGCD(a, m)
    if g != 1:
        raise ValueError(f"No modular inverse for {a} mod {m}")
    return x % m

def combine_congruences(a1, n1, a2, n2):
    """
    Combine two congruences:
      x ≡ a1 (mod n1)
      x ≡ a2 (mod n2)
    into one congruence:
      x ≡ a (mod n1*n2) (assuming n1, n2 coprime)
    """
    diff = (a2 - a1) % n2
    inv = modinv(n1, n2)
    k = (diff * inv) % n2
    combined_a = (a1 + k * n1) % (n1 * n2)
    combined_n = n1 * n2
    return combined_a, combined_n

def crt_stepwise(a_list, n_list):
    # Sort pairs by modulus descending
    pairs = sorted(zip(a_list, n_list), key=lambda x: x[1], reverse=True)
    a, n = pairs[0]
    for a_i, n_i in pairs[1:]:
        a, n = combine_congruences(a, n, a_i, n_i)
    return a, n

def main():
    k = int(input("Enter number of congruences: "))
    a_list = []
    n_list = []
    for i in range(k):
        a = int(input(f"Enter remainder a[{i+1}]: "))
        n = int(input(f"Enter modulus n[{i+1}]: "))
        a_list.append(a)
        n_list.append(n)

    # Check moduli are pairwise coprime (optional but recommended)
    from math import gcd
    for i in range(k):
        for j in range(i+1, k):
            if gcd(n_list[i], n_list[j]) != 1:
                print(f"Warning: moduli {n_list[i]} and {n_list[j]} are not coprime!")

    a, n = crt_stepwise(a_list, n_list)
    print(f"\nSolution:")
    print(f"x ≡ {a} mod {n}")

if __name__ == "__main__":
    main()
