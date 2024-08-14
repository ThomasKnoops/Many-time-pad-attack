import ciphers

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

def save_to_file(data, filename):
    with open(filename, 'w') as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")
    print(f"Data has been saved to {filename}")

def main():
    # Define the ciphertexts as hexadecimal strings
    ciphertexts = [
        ciphers.c1, ciphers.c2, ciphers.c3, ciphers.c4, ciphers.c5,
        ciphers.c6, ciphers.c7, ciphers.c8, ciphers.c9, ciphers.c10, 
        ciphers.T
    ]
    
    # Convert c3 to bytes for XOR operations
    c_bytes = hex_to_bytes(ciphers.c1)
    
    # Define the word to XOR with
    word = 'we can factor the number '
    
    results = {}

    # XOR each ciphertext with c3 and then XOR the result with 'the'
    for i, cipher in enumerate(ciphertexts):
        cipher_bytes = hex_to_bytes(cipher)
        result_after_c = xor_bytes(cipher_bytes, c_bytes)
        result_after_word = xor_with_word(result_after_c, word)
        
        # Convert result to readable string and check if it’s printable
        result_str = result_after_word.decode('utf-8', errors='ignore')
        
        results[f'Cipher {i + 1}'] = result_str
    
    # Save results to 'output.txt'
    save_to_file(results, 'output.txt')

if __name__ == "__main__":
    main()
