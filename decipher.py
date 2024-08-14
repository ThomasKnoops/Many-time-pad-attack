import helperFunctions as hf

def xor_with_word(xor_result_bytes, word):
    word_bytes = word.encode('utf-8')  # Convert word to bytes
    # XOR the result with the word bytes
    return hf.xor_bytes(xor_result_bytes, word_bytes)

def print_results(results):
    # Print the results in a readable format
    total_items = len(results)
    
    # Iterate over the dictionary with index
    for index, (key, value) in enumerate(results.items()):
        if index == total_items - 1:
            print(f"{key} (!Target Cipher!): {value}")
        else:
            print(f"{key}: {value}")

def decipher(scentence, start_cipher, cipher_array):    
    # Convert c to bytes for XOR operations
    c_bytes = hf.hex_to_bytes(start_cipher)    
    results = {}

    # XOR each ciphertext with c and then XOR the result with the scentence
    for i, cipher in enumerate(cipher_array):
        cipher_bytes = hf.hex_to_bytes(cipher)
        result_after_c = hf.xor_bytes(cipher_bytes, c_bytes)
        result_after_word = xor_with_word(result_after_c, scentence)
        
        # Convert result to readable string and check if it’s printable
        result_str = result_after_word.decode('utf-8', errors='ignore')
        
        results[f'Cipher {i + 1}'] = result_str
    print_results(results)
    return results