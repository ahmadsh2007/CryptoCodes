'''
In modern cryptography and cybersecurity, modular arithmetic plays a crucial role—particularly operations over prime fields. One such operation is computing modular square roots, which is directly tied to the concept of quadratic residues.
Given a large prime number p, an integer a is called a quadratic residue modulo p if there exists an integer x such that:
        x² ≡ a (mod p)

Not every value of a satisfies this condition. When no such x exists, a is referred to as a quadratic non-residue. The ability to determine whether a number is a quadratic residue has applications in primality testing, cryptographic protocols (like the Quadratic Residuosity Assumption), and more.
To test if a is a quadratic residue modulo an odd prime p, we use the Legendre symbol, denoted (a/p). It's defined as:
        (a/p) = 1 if a is a quadratic residue and a ≠ 0 mod p
        (a/p) = -1 if a is a quadratic non-residue
        (a/p) = 0 if a ≡ 0 mod p

Efficiently, the Legendre symbol can be computed with Euler's criterion:
        (a/p) ≡ a^((p-1)/2) mod p

If the result is 1, a is a quadratic residue. If the result is p - 1 (which is -1 mod p), then a is a non-residue.
Once a quadratic residue is identified, we can compute its square root modulo p. This is typically a hard problem in general settings, but it becomes straightforward when p ≡ 3 mod 4, which is true for many primes used in cryptography. In such cases, the square root of a modulo p can be calculated using the formula:
        x ≡ a^((p+1)/4) mod p

This formula follows from Fermat's Little Theorem and properties of quadratic residues in modular arithmetic. It's particularly useful when working with very large primes (e.g., 1024-bit or 2048-bit) as often used in cryptographic applications.
'''

def legendre_symbol(a, p):
    """Compute the Legendre symbol (a/p) using Euler's criterion"""
    return pow(a, (p - 1) // 2, p)

def modular_sqrt(a, p):
    """Compute the square root of a mod p assuming p ≡ 3 mod 4"""
    return pow(a, (p + 1) // 4, p)

def find_first_residue_sqrt(p, nums):
    for a in nums:
        if legendre_symbol(a, p) == 1:
            root = modular_sqrt(a, p)
            return max(root, p - root)  # return the larger root
    return None

def load_input(filename):
    """Load p and ints from a file formatted as:
       p = ...
       ints = [...]
    """
    with open(filename, "r") as f:
        content = f.read()
        
        p_line = next(line for line in content.splitlines() if line.strip().startswith("p"))
        p = int(p_line.split("=")[1].strip())

        # Extract ints list
        ints_line = next(line for line in content.splitlines() if line.strip().startswith("ints"))
        ints_str = ints_line.split("=")[1].strip()
        ints = eval(ints_str) 
        
        return p, ints

def main():
    input_file = r"input.txt"
    p, nums = load_input(input_file)
    
    result = find_first_residue_sqrt(p, nums)
    
    if result is not None:
        print("Modular square root found (larger root):", result)
    else:
        print("No quadratic residue found among the provided integers.")

if __name__ == "__main__":
    main()