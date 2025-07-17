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

from ASCII2Char import *


while True:
    choice = input("Encode or Decode: ")
    
    if choice.lower() == "encode":
        break
    if choice.lower() == "decode":
        break
