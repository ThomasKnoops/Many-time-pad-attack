import multiPadAttack as mpa
import decipher as dec

CIPHERS = []
T_CIPHER = ""

# This function will read all the ciphers from the file and store them in the CIPHERS list and read the target cipher
def read_ciphers():
    global CIPHERS, T_CIPHER
    with open('ciphers.txt', 'r') as file:
            for line in file:
                if line.startswith("c") or line.startswith("C"):
                    CIPHERS.append(line.split("= ")[1].strip())
                elif line.startswith("t") or line.startswith("T"):
                    T_CIPHER = line.split("= ")[1].strip()

def save_to_file(data, filename):
    with open(filename, 'w') as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")
    print(f"Data has been saved to {filename}")

if __name__ == "__main__":
    # Read the ciphers from the file
    read_ciphers()
    # Start interactive mode for searching the first word of any cipher
    input_word = input("Which word would you like to XOR at the beginning of the ciphers?: ")
    while True:
        mpa.multiPadAttack(input_word, CIPHERS)
        input_break = input("Try a new word, or stop searching? ([new word]/s): ")
        if input_break == "s":
            break
        else:
            input_word = input_break
    # Add the target cipher to the list of ciphers
    CIPHERS.append(T_CIPHER)
    # Start interactive mode for solving the cipher
    input_scentence = input("What is the scentence you would like to XOR with the ciphers?: ")
    input_cipher = input("From which cipher is this scentence the plaintext?: ")
    while True:
        results = dec.decipher(input_scentence, CIPHERS[int(input_cipher) - 1], CIPHERS)
        input_break = input("Try a new scentence, or stop solving? ([new scentence]/s): ")
        if input_break == "s":
            break
        else:
            input_scentence = input_break
            input_cipher = input("From which cipher is this scentence the plaintext?: ")
    # Save results to 'output.txt'
    save_to_file(results, 'output.txt')
    

