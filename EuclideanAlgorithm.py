'''
The Euclidean algorithm is a classic and efficient method for finding the greatest common divisor (GCD) of two integers.

Concept (How It Works)
Given two positive integers a and b:
1- Replace a with b, and b with a % b (the remainder).
2- Repeat step 1 until b == 0.
3- When b == 0, a is the GCD.

Greatest Common Divisor (GCD)

You can do it in 2 main ways in coding and here it is.
'''

def GCDRecursive(a: int, b: int) -> int:
    """
    Recursive implementation of the Euclidean algorithm.
    Returns a when b is equal to zero, otherwise recurses with (b, a % b).
    """
    return a if b == 0 else GCDRecursive(b, a % b)

def GCDWhileLoop(a: int, b: int) -> int:
    """
    Iterative implementation of the Euclidean algorithm using a while loop.
    Swaps and reduces until b is zero.
    """
    while b != 0:
        a, b = b, a % b
    return a


def main() -> None:
    a: int = int(input("Enter number a: "))
    b: int = int(input("Enter number b: "))
    if a <= 0 or b <= 0:
        print("Please enter positive integers only.")
        return
    print(GCDWhileLoop(a, b))
    return
    print(GCDRecursive(a, b))

if __name__ == '__main__':
    main()