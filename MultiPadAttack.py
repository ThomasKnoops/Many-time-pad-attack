import ciphers

def xor_bytes(b1, b2):
    # Determine the length of the shorter byte array
    min_length = min(len(b1), len(b2))
    # XOR the bytes of the two arrays up to the minimum length
    return bytes([x ^ y for x, y in zip(b1[:min_length], b2[:min_length])])

def hex_to_bytes(hex_string):
    # Convert a hexadecimal string to bytes
    return bytes.fromhex(hex_string)

def test_word_at_start(xor_result_bytes, word):
    word_bytes = word.encode('utf-8')  # Convert word to bytes
    # Test only starting at the beginning
    start = 0
    if len(xor_result_bytes) >= len(word_bytes):
        slice_bytes = xor_result_bytes[start:start + len(word_bytes)]
        test_result = xor_bytes(slice_bytes, word_bytes)
        test_result_str = test_result.decode('utf-8', errors='ignore')
        
        # Print results if readable
        if test_result_str.isprintable() and len(test_result_str.strip()) > 0:
            print(f"Test Result (String): '{test_result_str}'")
            print(f"Test Result (Hex): {test_result.hex().upper()}")
        else:
            print(f"Word '{word}' does not match at the beginning of the XOR result.")
        print()

def main():
    # Define the ciphertexts as hexadecimal strings
    ciphertexts = [
        ciphers.c1, ciphers.c2, ciphers.c3, ciphers.c4, ciphers.c5,
        ciphers.c6, ciphers.c7, ciphers.c8, ciphers.c9, ciphers.c10
    ]

    # Define the word to test
    word = 'the'

    # XOR every pair of ciphers and test the result
    for i in range(len(ciphertexts)):
        for j in range(len(ciphertexts)):
            c1 = hex_to_bytes(ciphertexts[i])
            c2 = hex_to_bytes(ciphertexts[j])
            
            # XOR the selected ciphers
            result = xor_bytes(c1, c2)
            
            # Print result as hexadecimal string
            result_hex = result.hex()
            print(f"{i + 1}:")

            # Test the word against the XOR result
            test_word_at_start(result, word)

if __name__ == "__main__":
    main()
