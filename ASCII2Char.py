def encode() -> list[int]:
        encode = "Hello, World!"
        encoded = []
        for i in range(len(encode)):
            encoded.append(ord(encode[i]))
        return encoded

def decode() -> str:
    decode = [72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]
    decoded = ""
    for i in range(len(decode)):
        decoded += chr(decode[i])
    return decoded

def main() -> None:
    while True:
        choice = input("Encode or Decode: ")
        if choice.lower() == "encode":
            print(encode())
            break
        if choice.lower() == "decode":
            print(decode())
            break


if __name__ == '__main__':
    main()