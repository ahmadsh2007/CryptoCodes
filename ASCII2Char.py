def encode(Plaintext) -> list[int]:
        encoded = []
        for i in range(len(Plaintext)):
            encoded.append(ord(Plaintext[i]))
        return encoded

def decode(Ciphertext) -> str:
    decoded = ""
    for i in range(len(Ciphertext)):
        decoded += chr(Ciphertext[i])
    return decoded

def main() -> None:
    while True:
        choice = input("Encode or Decode: ")
        if choice.lower() == "encode":
            Plaintext = "Hello, World!"
            print(encode(Plaintext))
            break
        if choice.lower() == "decode":
            Ciphertext = [72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]
            print(decode(Ciphertext))
            break


if __name__ == '__main__':
    main()