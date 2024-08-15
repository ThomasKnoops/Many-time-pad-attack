import multiPadAttack as mpa
import decipher as dec
import helperFunctions as help
import tkinter as tk
from tkinter import ttk

# Ciphet global variables
CIPHERS = []
T_CIPHER = ""

# Create the main application window and set the title
ROOT = tk.Tk()
ROOT.title("Multi Pad Attack")

# Gui global variables
current_frame = None
text_area = None
target_value = tk.IntVar(value=0)
combobox_value = None

def setup_gui_screen_1():
    global current_frame, text_area, target_value, combobox_value
    # Create a frame using ttk
    current_frame = ttk.Frame(ROOT, padding=10)
    current_frame.grid(sticky="nsew")  # Ensure it stretches with the window

    # Add a label
    ttk.Label(current_frame, text="Paste all your ciphers in this textbox. Only 1 per line. If you have a specific target cipher, make sure it is the last one!").grid(column=0, row=0, pady=(0, 10))

    # Create a text area with a scrollbar
    text_frame = ttk.Frame(current_frame)
    text_frame.grid(column=0, row=1, sticky="nsew")  # Expand in both directions

    text_area = tk.Text(text_frame, wrap='word', height=15, width=50)
    text_area.grid(column=0, row=0, sticky="nsew")

    scrollbar = ttk.Scrollbar(text_frame, orient='vertical', command=text_area.yview)
    scrollbar.grid(column=1, row=0, sticky='ns')
    text_area.config(yscrollcommand=scrollbar.set)

    current_frame.rowconfigure(1, weight=1)
    current_frame.columnconfigure(0, weight=1)
    text_frame.rowconfigure(0, weight=1)
    text_frame.columnconfigure(0, weight=1)

    # Add a target checkbox with an initially unchecked state
    ttk.Checkbutton(current_frame, text="Is there a Target?", variable=target_value).grid(column=0, row=2, pady=(10, 0))

    # Add combobox for the type of ciphers
    combobox_value = ttk.Combobox(current_frame, values=["Plaintext", "Hexadecimal", "Binary"], state="readonly")
    combobox_value.set("Plaintext")
    combobox_value.grid(column=0, row=3, pady=(10, 0))

    # Add buttons
    button_frm = ttk.Frame(current_frame)
    button_frm.grid(column=0, row=4, pady=(10, 0))  # Center the buttons under the text area

    ttk.Button(button_frm, text="Start", command=read_ciphers).grid(column=0, row=0, pady=(10, 0))
    ttk.Button(button_frm, text="Quit", command=ROOT.destroy).grid(column=1, row=0, pady=(10, 0))

# Get all the ciphers from the text area
def read_ciphers():
    global CIPHERS, T_CIPHER, text_area, target_value, combobox_value
    CIPHERS = []
    T_CIPHER = ""
    text_content = text_area.get("1.0", "end-1c")
    lines = text_content.splitlines()
    match combobox_value.get():
        case "Plaintext":
            for i, line in enumerate(lines):
                hex_value = help.plain_to_hex(line.strip())
                if i == len(lines) - 1 and target_value.get() == 1:
                    T_CIPHER = hex_value
                else:
                    CIPHERS.append(hex_value)

        case "Hexadecimal":
            for i, line in enumerate(lines):
                hex_value = line.strip()  # Already in hex format
                if i == len(lines) - 1 and target_value.get() == 1:
                    T_CIPHER = hex_value
                else:
                    CIPHERS.append(hex_value)

        case "Binary":
            for i, line in enumerate(lines):
                # Convert binary string to plaintext, then to hex
                hex_value = help.binary_to_hex(line.strip())
                if i == len(lines) - 1 and target_value.get() == 1:
                    T_CIPHER = hex_value
                else:
                    CIPHERS.append(hex_value)


    print(CIPHERS)
    print(T_CIPHER)

def setup_gui_screen_2():
    global current_frame
    if current_frame:
        current_frame.destroy()

    # Create a frame using ttk
    current_frame = ttk.Frame(ROOT, padding=10)
    current_frame.grid(sticky="nsew")

    # Add new widgets
    ttk.Label(current_frame, text="The ciphers have been processed. Now perform the next steps.").grid(column=0, row=0, pady=(0, 10))
    
    # Example new widgets: you can add any widgets here as needed
    ttk.Button(current_frame, text="Proceed", command=try_first_word).grid(column=0, row=1, pady=(10, 0))
    ttk.Button(current_frame, text="Quit", command=ROOT.destroy).grid(column=1, row=1, pady=(10, 0))

    # Configure grid stretching
    current_frame.rowconfigure(0, weight=1)
    current_frame.columnconfigure(0, weight=1)

def try_first_word():
    pass

def save_to_file(data, filename):
    with open(filename, 'w') as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")
    print(f"Data has been saved to {filename}")

if __name__ == "__main__":
    setup_gui_screen_1()
    ROOT.mainloop()

    
    # Start interactive mode for searching the first word of any cipher
    # input_word = input("Which word would you like to XOR at the beginning of the ciphers?: ")
    # while True:
    #     mpa.multiPadAttack(input_word, CIPHERS)
    #     input_break = input("Try a new word, or stop searching? ([new word]/s): ")
    #     if input_break == "s":
    #         break
    #     else:
    #         input_word = input_break
    # # Add the target cipher to the list of ciphers
    # if T_CIPHER:
    #     CIPHERS.append(T_CIPHER)
    # # Start interactive mode for solving the cipher
    # input_scentence = input("What is the scentence you would like to XOR with the ciphers?: ")
    # input_cipher = input("From which cipher is this scentence the plaintext?: ")
    # while True:
    #     results = dec.decipher(input_scentence, CIPHERS[int(input_cipher) - 1], CIPHERS)
    #     input_break = input("Try a new scentence, or stop solving? ([new scentence]/s): ")
    #     if input_break == "s":
    #         break
    #     else:
    #         input_scentence = input_break
    #         input_cipher = input("From which cipher is this scentence the plaintext?: ")
    # # Save results to 'output.txt'
    # save_to_file(results, 'output.txt')
    

