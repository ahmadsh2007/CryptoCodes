while True:
    choice = input("Encode or Decode: ")

    if choice.lower() == "encode":
        encode = 'Hello, World!'
        encoded = encode.encode('utf-8').hex()
        print(f"Encoded: {encoded}")
        break
    
    if choice.lower() == "decode":
        decode = "48656c6c6f2c20576f726c6421"
        decoded = bytes.fromhex(decode).decode('utf-8')
        print(f"Decoded: {decoded}")
        break