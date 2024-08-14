import helperFunctions as hf

# XOR the result with the word bytes
def xor_with_word(xor_result_bytes, word):
    word_bytes = word.encode('utf-8')
    return hf.xor_bytes(xor_result_bytes, word_bytes)

# Print the results in a readable format, and give the target cipher a special mark
def print_results(results):
    total_items = len(results)
    
    for index, (key, value) in enumerate(results.items()):
        if index == total_items - 1:
            print(f"{key} (!Target Cipher!): {value}")
        else:
            print(f"{key}: {value}")

# Decipher the target cipher using the sentences and all the ciphers, interactively
def decipher(sentence, start_cipher, cipher_array):    
    start_cipher_bytes = hf.hex_to_bytes(start_cipher)
    results = {}

    # XOR each ciphertext with start_cipher and then XOR the result with the sentence
    for i, cipher in enumerate(cipher_array):
        cipher_bytes = hf.hex_to_bytes(cipher)
        result_after_XOR_1 = hf.xor_bytes(cipher_bytes, start_cipher_bytes)
        result_after_XOR_2 = xor_with_word(result_after_XOR_1, sentence)
        
        result_str = result_after_XOR_2.decode('utf-8', errors='ignore')
        results[f'Cipher {i + 1}'] = result_str

    print_results(results)
    return results