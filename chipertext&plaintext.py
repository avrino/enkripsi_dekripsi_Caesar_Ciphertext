import tkinter as tk

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            char_code = ord(char)
            char_code = (char_code - ord('a') + shift) % 26 + ord('a')
            if is_upper:
                char_code -= 32
            char = chr(char_code)
        result += char
    return result

def encrypt():
    text = input_text.get("1.0", "end-1c")
    shift = int(shift_value.get())
    encrypted_text = caesar_cipher(text, shift)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", encrypted_text)

def decrypt():
    text = input_text.get("1.0", "end-1c")
    shift = int(shift_value.get())
    decrypted_text = caesar_cipher(text, -shift)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", decrypted_text)

app = tk.Tk()
app.title("Caesar Ciphertext Encryption/Decryption")
app.geometry('350x500')

input_label = tk.Label(app, text="Masukan Text :")
input_label.pack()

input_text = tk.Text(app, width=35, height=10)
input_text.pack()

shift_label = tk.Label(app, text="Jumlah Pergeseran :")
shift_label.pack()

shift_value = tk.Entry(app)
shift_value.pack()

encrypt_button = tk.Button(app, text="Encode", command=encrypt)
encrypt_button.pack()

decrypt_button = tk.Button(app, text="Decode", command=decrypt)
decrypt_button.pack()

output_label = tk.Label(app, text="Hasil :")
output_label.pack()

output_text = tk.Text(app, width=35, height=10)
output_text.pack()

app.mainloop()