import helperFunctions as hf

def test_word_at_start(xor_result_bytes, word):
    word_bytes = word.encode('utf-8')  # Convert word to bytes
    # Test only starting at the beginning
    if len(xor_result_bytes) >= len(word_bytes):
        slice_bytes = xor_result_bytes[:len(word_bytes)]
        test_result = hf.xor_bytes(slice_bytes, word_bytes)
        test_result_str = test_result.decode('utf-8')
        
        # Return results if readable
        if test_result_str.isprintable() and len(test_result_str.strip()) > 0:
            return True, f"Test Result (String): '{test_result_str}'\n"
        else:
            return False, ""

def multiPadAttack(word, ciphertexts):
    # XOR every pair of ciphers and test the result
    for i in range(len(ciphertexts)):
        final_result_string = ""
        go_on = True
        for j in range(len(ciphertexts)):
            c1 = hf.hex_to_bytes(ciphertexts[i])
            c2 = hf.hex_to_bytes(ciphertexts[j])
            
            # XOR the selected ciphers
            xorred_cipher = hf.xor_bytes(c1, c2)

            # Test the word against the XOR result
            go_on, result_string = test_word_at_start(xorred_cipher, word)
            if go_on:
                final_result_string += f"XOR between c{i + 1} and c{j + 1}: {result_string}"
            else:
                print(f"XOR between c{i + 1} and word: '{word}' does not always produce a readable string.")
                break
        if go_on:
            print(final_result_string)
