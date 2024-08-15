import helperFunctions as hf

# XOR the result with the word bytes
def xor_with_word(xor_result_bytes, word):
    word_bytes = word.encode('utf-8')
    return hf.xor_bytes(xor_result_bytes, word_bytes)


# Decipher the target cipher using the sentences and all the ciphers, interactively
def decipher(sentence, start_cipher, cipher_array):    
    start_cipher_bytes = hf.hex_to_bytes(start_cipher)
    results_string = []

    # XOR each ciphertext with start_cipher and then XOR the result with the sentence
    for i, cipher in enumerate(cipher_array):
        cipher_bytes = hf.hex_to_bytes(cipher)
        result_after_XOR_1 = hf.xor_bytes(cipher_bytes, start_cipher_bytes)
        result_after_XOR_2 = xor_with_word(result_after_XOR_1, sentence)
        
        result_str = result_after_XOR_2.decode('utf-8', errors='ignore')
        results_string.append(result_str)

    return results_string