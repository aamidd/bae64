alpha = [chr(i) for i in range(ord('A'), ord('Z') + 1)] + [chr(i) for i in range(ord('a'), ord('z') + 1)] + [str(i) for i in range(10)] + ['+', '/']

def tobin(s):
    result = ""
    for c in s:
        result += f"{ord(c):08b}"
    return result

def tobae64(s):
    binary = tobin(s)
    pad = (6 - (len(binary) % 6)) % 6
    binary += "0" * pad
    pad = pad // 2

    bae64 = ""
    for i in range(0, len(binary), 6):
        bae64 += alpha[int(binary[i:i+6], 2)]
    bae64 += "=" * pad
    return bae64


s = input("convert > ")

print(tobae64(s))
