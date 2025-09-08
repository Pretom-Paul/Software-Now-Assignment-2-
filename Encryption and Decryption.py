# My Raw Text Location : C:\Users\joy43\Desktop\New folder\Assignment 2\Qus 1\raw_text.txt

# Encrypt a single character

def encrypted_character(character, shift1, shift2):
    if character.islower():
        if 'a' <= character <= 'm':
            return chr((ord(character) - ord('a') + (shift1 * shift2)) % 26 + ord('a'))
        else:
            return chr((ord(character) - ord('a') - (shift1 + shift2)) % 26 + ord('a'))
    elif character.isupper():
        if 'A' <= character <= 'M':
            return chr((ord(character) - ord('A') - shift1) % 26 + ord('A'))
        else:
            return chr((ord(character) - ord('A') + (shift2 ** 2)) % 26 + ord('A'))
    else:
        return character

# Decrypt a single character (reverse of encryption)

def decrypted_character(character, shift1, shift2):
    if character.islower():
        if 'a' <= character <= 'm':
            return chr((ord(character) - ord('a') - (shift1 * shift2)) % 26 + ord('a'))
        else:
            return chr((ord(character) - ord('a') + (shift1 + shift2)) % 26 + ord('a'))
    elif character.isupper():  
        if 'A' <= character <= 'M':
            return chr((ord(character) - ord('A') + shift1) % 26 + ord('A'))
        else:
            return chr((ord(character) - ord('A') - (shift2 ** 2)) % 26 + ord('A'))
    else:
        return character

# Encrypt the full text file

def encrypt_file(shift1, shift2):
    with open(r"C:\Users\joy43\Desktop\New folder\Assignment 2\Qus 1\raw_text.txt", "r") as f:    
        text = f.read()  
    encrypted = ''.join(encrypted_character(character, shift1, shift2) for character in text)
    with open(r"C:\Users\joy43\Desktop\New folder\Assignment 2\Qus 1\encrypted_text.txt", "w") as f:
        f.write(encrypted)  

# Decrypt the full text file

def decrypt_file(shift1, shift2):
    with open(r"C:\Users\joy43\Desktop\New folder\Assignment 2\Qus 1\encrypted_text.txt", "r") as f:
        text = f.read()  
    decrypted = ''.join(decrypted_character(character, shift1, shift2) for character in text)
    with open(r"C:\Users\joy43\Desktop\New folder\Assignment 2\Qus 1\decrypted_text.txt", "w") as f:
        f.write(decrypted) 

# Verification function

def verify():
    with open(r"C:\Users\joy43\Desktop\New folder\Assignment 2\Qus 1\raw_text.txt") as f1,\
     open(r"C:\Users\joy43\Desktop\New folder\Assignment 2\Qus 1\decrypted_text.txt") as f2:
        return f1.read() == f2.read()  

# Main Program Execution
# Ask user for two shift values

if __name__ == "__main__":
    s1 = int(input("Enter shift1: "))
    s2 = int(input("Enter shift2: "))

# Encrypt raw_text.txt to encrypted_text.txt

    encrypt_file(s1, s2)

# Decrypt encrypted_text.txt to decrypted_text.txt

    decrypt_file(s1, s2)

# Verify decryption

    if verify():
        print("Decryption Successful")
    else:
        print("Decryption Failed")
