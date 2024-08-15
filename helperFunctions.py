# Convert a hexadecimal string to bytes
def hex_to_bytes(hex_string):
    return bytes.fromhex(hex_string)

# XOR two byte arrays, up to the length of the shortest
def xor_bytes(b1, b2):
    min_length = min(len(b1), len(b2))
    return bytes([x ^ y for x, y in zip(b1[:min_length], b2[:min_length])])

# Convert a plaintext string to hexadecimal
def plain_to_hex(plain_text):
    return plain_text.encode('utf-8').hex()

# Convert a binary string to hexadecimal
def binary_to_hex(binary_string):
    hex_value = hex(int(binary_string, 2))[2:]
    if len(hex_value) % 2 != 0:
        hex_value = "0" + hex_value
    return hex_value