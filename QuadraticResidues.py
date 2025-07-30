'''
In modular arithmetic, taking the square root of a number modulo a prime p means finding \
an integer a such that a ^ 2 ≡ x mod p. In other words, when a is squared and reduced modulo p, \
the result is x. If such an a exists, we say that x is a quadratic residue modulo p. Otherwise, \
x is a quadratic non-residue. For every quadratic residue, there are always two square roots: a \
and p - a, since both give the same result when squared modulo p. For example, with p = 29, \
if a = 11, then 11 ^ 2 mod 29 = 121 mod 29 = 5, so 11 is a square root of 5 modulo 29. \
Similarly, -11 and 18 are valid square root of 5 modulo 29. Quadratic residues only make up \
about half the elements in the set F_p^* (all integers from 1 to p - 1), and checking for \
them can be done by brute force when p is small.
'''

def is_quadratic_residue(x, p):
    """
    Check if x is a quadratic residue modulo p using Euler's Criterion.
    Returns True if residue, False otherwise.
    """
    return pow(x, (p - 1) // 2, p) == 1

def find_square_roots(x, p):
    """
    Find the two square roots of x modulo p.
    Assumes x is a quadratic residue mod p.
    Returns a tuple (root1, root2) where root2 = p - root1.
    """
    for a in range(1, p):
        if (a * a) % p == x % p:
            return (a, p - a)
    return None

def main():
    p = int(input("Enter prime modulus p: "))
    numbers_input = input("Enter numbers separated by spaces: ")
    numbers = list(map(int, numbers_input.strip().split()))

    print(f"Prime modulus: {p}\n")

    for x in numbers:
        print(f"Checking number: {x}")
        if is_quadratic_residue(x, p):
            roots = find_square_roots(x, p)
            if roots:
                root1, root2 = roots
                smaller_root = min(root1, root2)
                print(f"  Quadratic residue modulo {p}")
                print(f"  Square roots: {root1} and {root2}")
                print(f"  Smaller root (flag): {smaller_root}\n")
            else:
                print(f"  Error: Could not find square roots for {x}\n")
        else:
            print(f"  Not a quadratic residue modulo {p}\n")

if __name__ == "__main__":
    main()