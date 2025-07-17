while True:
    choice = input("Encode or Decode: ")
    if choice.lower() == "encode":
        encode = "Hello, Wordl!"
        encoded = []
        for i in range(len(encode)):
            encoded.append(ord(encode[i]))
        print(encoded)
        break
    if choice.lower() == "decode":
        decode = [72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 100, 108, 33]
        decoded = ""
        for i in range(len(decode)):
            decoded += chr(decode[i])
        print(decoded)
        break