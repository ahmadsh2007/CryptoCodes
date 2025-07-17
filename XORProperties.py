'''
Commutative: A ⊕ B = B ⊕ A
Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
Identity: A ⊕ 0 = A
Self-Inverse: A ⊕ A = 0
'''

'''
Find the flag:

KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

NB, Before you XOR these objects, be sure to decode from hex to bytes.
'''

from pwn import xor

key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
key2 = xor(bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"), key1)
key3 = xor(bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"), key2)
flag = xor(xor(bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"), key1), bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")) 
print(key1)
print(key2)
print(key3)
print(flag)