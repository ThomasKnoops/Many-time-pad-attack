def hex_to_bytes(hex_string):
    # Convert a hexadecimal string to bytes
    return bytes.fromhex(hex_string)

def xor_bytes(b1, b2):
    # Determine the length of the shorter byte array
    min_length = min(len(b1), len(b2))
    # XOR the bytes of the two arrays up to the minimum length
    return bytes([x ^ y for x, y in zip(b1[:min_length], b2[:min_length])])

def xor_with_word(xor_result_bytes, word):
    word_bytes = word.encode('utf-8')  # Convert word to bytes
    # XOR the result with the word bytes
    return xor_bytes(xor_result_bytes, word_bytes)

def print_results(results):
    # Print the results in a readable format
    total_items = len(results)
    
    # Iterate over the dictionary with index
    for index, (key, value) in enumerate(results.items()):
        if index == total_items - 1:
            print(f"{key} (/ Target Cipher!): {value}")
        else:
            print(f"{key}: {value}")

def decipher(scentence, start_cipher, cipher_array):    
    # Convert c to bytes for XOR operations
    c_bytes = hex_to_bytes(start_cipher)    
    results = {}

    # XOR each ciphertext with c and then XOR the result with the scentence
    for i, cipher in enumerate(cipher_array):
        cipher_bytes = hex_to_bytes(cipher)
        result_after_c = xor_bytes(cipher_bytes, c_bytes)
        result_after_word = xor_with_word(result_after_c, scentence)
        
        # Convert result to readable string and check if it’s printable
        result_str = result_after_word.decode('utf-8', errors='ignore')
        
        results[f'Cipher {i + 1}'] = result_str
    print_results(results)
    return results