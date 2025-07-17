'''
XOR is a bitwise operator which returns 0 if the bits are the same, and 1 otherwise. In textbooks the XOR operator is denoted by ⊕, but in most challenges and programming languages you will see the caret ^ used instead.

A	B	Output
0	0	0
0	1	1
1	0	1
1	1	0

For longer binary numbers we XOR bit by bit: 0110 ^ 1010 = 1100. We can XOR integers by first converting the integer from decimal to binary. We can XOR strings by first converting each character to the integer representing the Unicode character.
'''

def XOR(message, key):
    result = ''
    for char in message:
        result += chr(ord(char) ^ key)
    return result

def main():
    plaintext = 'Hello, World!'
    key = 13

    ciphertext = XOR(plaintext, key)
    print(f'Ciphertext: {ciphertext}')

    decrypted = XOR(ciphertext, key)
    print(f'Decrypted:  {decrypted}')

if __name__ == '__main__':
    main()