'''
Imagine you lean over and look at a cryptographer's notebook. You see some notes in the margin:
        4 + 9 = 1
        5 - 7 = 10
        2 + 3 = 5
At first you might think they've gone mad. Maybe this is why there are so many data leaks nowadays you'd think, but this is nothing more than modular arithmetic modulo 12 (albeit with some sloppy notation).

NB: in programming, % means mod (modulo)

You may not have been calling it modular arithmetic, but you've been doing these kinds of calculations since you learnt to tell the time (look again at those equations and think about adding hours).
Formally, "calculating time" is described by the theory of congruences. We say that two integers are congruent modulo m if a ≡ b mod m

Another way of saying this, is that when we divide the integer a by m, the remainder is b. This tells you that if m divides a (this can be written as m|a) then a ≡ 0 mod m.

To calculate 8146798528947 ≡ X mod 17, we start with current = 0. Then for each digit d in the number, we update current: current = (current * 10 + d) mod 17
At the end, current will hold the remainder X
NB: digits should be access from left to right
'''

def moduloCalc(X: int, m: int) -> int:
    '''
    This function calculates the value of Y in X ≡ Y mod m
    '''
    current: int = 0
    for d in str(X):
        # print(int(d))
        current = (current * 10 + int(d)) % m
    return current

def main() -> None:
    X: int = int(input("to calculate the value of Y in (X ≡ Y mod m), Enter the value of X: "))
    m: int = int(input("Enter the value of m: "))
    print(moduloCalc(X, m))

if __name__ == '__main__':
    main()