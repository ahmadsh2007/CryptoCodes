/*
XOR is a bitwise operator which returns 0 if the bits are the same, and 1 otherwise. In textbooks the XOR operator is denoted by ⊕, but in most challenges and programming languages you will see the caret ^ used instead.

A	B	Output
0	0	0
0	1	1
1	0	1
1	1	0

For longer binary numbers we XOR bit by bit: 0110 ^ 1010 = 1100. We can XOR integers by first converting the integer from decimal to binary. We can XOR strings by first converting each character to the integer representing the Unicode character.
*/
#include <iostream>
#include <string>
#include <iomanip>

std::string XOR(std::string message, int key);

int main(){
    std::string plaintext = "Hello, World!";
    int key = 13;

    std::string encrypted  = XOR(plaintext, key);
    std::cout << "Encrypted (as string): " << encrypted << '\n';
    std::cout << "Encrypted (hex): ";
    for (unsigned char c : encrypted) {
        std::cout << std::hex << std::setw(2) << std::setfill('0') << (int)c << " ";
    }
    std::cout << std::dec << std::endl;

    std::string decrypted  = XOR(encrypted, key);
    std::cout << "Plaintext: " << decrypted << '\n';

    return 0;
}

std::string XOR(std::string message, int key){
    std::string result;
    for (char c : message) {
        result += static_cast<char>(c ^ key);
    }

    return result;
}