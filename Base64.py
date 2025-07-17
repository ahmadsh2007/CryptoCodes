import base64

while True:
    choice = input("Encode or Decode: ")

    if choice.lower() == "encode":
        encode = b"Hello, Wordl!"
        encoded = base64.b64encode(encode)
        print(encoded)
        break

    if choice.lower() == "decode":
        decode = b'SGVsbG8sIFdvcmRsIQ=='
        decoded = base64.b64decode(decode)
        print(decoded)
