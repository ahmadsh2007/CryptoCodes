'''
Cryptosystems like RSA works on numbers, but messages are made up of characters. How shou-
ld we convert our messages into numbers so that mathematical operations can be applied?
The most common way is to take the ordinal bytes of the message, convert them into hexade-
cimal, and concatenate. This can be interpreted as a base-16/hexadecimal number, and also
represented in base-10/decimal.
To illustrate:

message: HELLO
ascii bytes: [72, 69, 76, 76, 79]
hex bytes: [0x48, 0x45, 0x4c, 0x4c, 0x4f]
base-16: 0x48454c4c4f
base-10: 310400273487
'''

def message2Number(message):
    ascii_bytes = [ord(char) for char in message]

    hex_bytes = [format(byte, '02x') for byte in ascii_bytes]

    hex_string = ''.join(hex_bytes)

    decimal_number = int(hex_string, 16)

    print(f"Message      : {message}")
    print(f"ASCII bytes  : {ascii_bytes}")
    print(f"Hex bytes    : {[f'0x{h}' for h in hex_bytes]}")
    print(f"Base-16 hex  : 0x{hex_string}")
    print(f"Base-10 dec  : {decimal_number}")
    
    return decimal_number

def number2Message(number):
    hex_string = format(number, 'x')

    if len(hex_string) % 2 != 0:
        hex_string = '0' + hex_string

    hex_bytes = [hex_string[i:i+2] for i in range(0, len(hex_string), 2)]

    message = ''.join(chr(int(byte, 16)) for byte in hex_bytes)

    print(f"Base-10 dec  : {number}")
    print(f"Base-16 hex  : 0x{hex_string}")
    print(f"Hex bytes    : {[f'0x{b}' for b in hex_bytes]}")
    print(f"ASCII bytes  : {[int(b, 16) for b in hex_bytes]}")
    print(f"Message      : {message}")

    return message

def main() -> None:
    while True:
        choice = input("Encode or Decode: ")
        if choice.lower() == "encode":
            Plaintext = 'HELLO'
            print(message2Number(Plaintext))
            break
        if choice.lower() == "decode":
            Ciphertext = 310400273487
            print(number2Message(Ciphertext))
            break


if __name__ == '__main__':
    main()
