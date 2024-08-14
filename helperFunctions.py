def hex_to_bytes(hex_string):
    # Convert a hexadecimal string to bytes
    return bytes.fromhex(hex_string)

def xor_bytes(b1, b2):
    # Determine the length of the shorter byte array
    min_length = min(len(b1), len(b2))
    # XOR the bytes of the two arrays up to the minimum length
    return bytes([x ^ y for x, y in zip(b1[:min_length], b2[:min_length])])
