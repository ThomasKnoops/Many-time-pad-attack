# Convert a hexadecimal string to bytes (ciphers are given in hexadecimal format)
def hex_to_bytes(hex_string):
    return bytes.fromhex(hex_string)

# XOR two byte arrays, up to the length of the shortest
def xor_bytes(b1, b2):
    min_length = min(len(b1), len(b2))
    return bytes([x ^ y for x, y in zip(b1[:min_length], b2[:min_length])])
