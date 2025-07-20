/*
The Euclidean Algorithm is a way to find the greatest common divisor (GCD) of two integers, say a and b, \
using division and remainders. It works by repeatedly replacing the larger number with its remainder when \
divided by the smaller one. For example, if a = 30 and b = 12, we start with:

                            30 = 2 * 12 + 6
                            12 = 2 * 6 + 0

When the remainder hits 0, we stop. The last non-zero remainder is the GCD, in this case, 6. That's the basic Euclidean Algorithm.
The Extended Euclidean Algorithm does more: it finds integers u and v such that:

                            a * u + b * v = gcd(a, b)
    
This is called Bézout's identity, and these coefficients u and v can be extremely useful — especially when \
working in modular arithmetic, like in RSA encryption.
To find these coefficients, we don't just calculate the remainders — we also keep track of how each remainder \
is made using previous remainders, going all the way back to a and b. We do this using a table.

Let's look at the example a = 30, b = 12, which has GCD = 6. We'll construct a table with five columns: the \
step number, the remainder r, the quotient q, and two coefficients x, y representing how each remainder is  \
written as a combination of a and b.

Here's the full table:
| Step | r  | q | x | y  |
| ---- | -- | - | - | -- |
| 0    | 30 | — | 1 | 0  |
| 1    | 12 | — | 0 | 1  |
| 2    | 6  | 2 | 1 | -2 |
| 3    | 0  | 2 | — | —  |

Each row calculates a new remainder:
For step 2:
                r = 30 - 2 * 12 = 6

and the corresponding coefficients:
                x = 1 = 1 * 30 + (-2) * 12

This tells us:
                30 * 1 + 12 * (-2) = 6

The algorithm ends here, since we've reached remainder 0 in step 3. The last non-zero remainder is the GCD, and the x and y values in that row (step 2) are the u and v from Bézout's identity.

Now let's try a slightly bigger pair: a = 101, b = 23. Run the Euclidean algorithm:
                101 = 4 * 23 + 9
                23  = 2 * 9  + 5
                9   = 1 * 5  + 4
                5   = 1 * 4  + 1
                4   = 1 * 4  + 0

The GCD is 1. Let's build the table backward to find coefficients:
| Step | r   | q | x  | y   |
| ---- | --- | - | -- | --- |
| 0    | 101 | — | 1  | 0   |
| 1    | 23  | — | 0  | 1   |
| 2    | 9   | 4 | 1  | -4  |
| 3    | 5   | 2 | -2 | 9   |
| 4    | 4   | 1 | 3  | -13 |
| 5    | 1   | 1 | -5 | 22  |

This final row gives:
                1 = 101 * (-5) + 23 * 22

So u = -5, v = 22, and it satisfies Bézout's identity.
The logic behind the x and y columns is recursive: at each step, the x and y are calculated as:
                X_n = X_{n-2} - q_{n-1} * X_{n-1}
                Y_n = Y_{n-2} - q_{n-1} * Y_{n-1}
We start with base cases:
              - X_0 = 1, Y_0 = 0
              - X_1 = 0, Y_1 = 1

Then we compute each new x, y using the formula above.
This process is entirely deterministic and leads us to the smallest integer combination of a and b that equals their GCD.
If a and b are coprime, the result is always 1, and the algorithm will give you values that are inverses of one another \
modulo a or b, depending on your goal.

DIDN'T UNDERSTAND??? Check: https://youtu.be/6KmhCKxFWOs
*/
#include <stdio.h>

// Function declaration
long long extendedGCD(long long a, long long b, long long *x, long long *y);

int main(void){
    long long a, b;
    printf("p: ");
    scanf("%lld", &a);

    printf("q: ");
    scanf("%lld", &b);

    long long gcd, x, y;
    gcd = extendedGCD(a, b, &x, &y);

    printf("GCD(%lld, %lld) = %lld\n", a, b, gcd);
    printf("Coefficients x and y such that %lld * x + %lld * y = GCD:\n", a, b);
    printf("x = %lld, y = %lld\n", x, y);
    printf("%lld * %lld + %lld * %lld = %lld\n", a, x, b, y, a * x + b * y);

    return 0;
}

long long extendedGCD(long long a, long long b, long long *x, long long *y){
    if (b == 0){
        *x = 1;
        *y = 0;
        return a;
    }

    long long x1, y1;
    long long gcd = extendedGCD(b, a % b, &x1, &y1);

    *x = y1;
    *y = x1 - (a / b) * y1;

    return gcd;
}