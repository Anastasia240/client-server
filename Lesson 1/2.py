import binascii

strs = [b'class', b'function', b'method']

for s in strs:
    print(type(s), binascii.hexlify(s), len(s))
