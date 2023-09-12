from cryptography.fernet import Fernet

def encrypt_message(message, key):
    """
    Encrypts a message using a key
    """
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message

def decrypt_message(encrypted_message, key):
    """
    Decrypts an encrypted message using a key
    """
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()

def generate_key():
    """
    Generates a key for encryption and decryption
    """
    key = Fernet.generate_key()
    return key

def write_key(key, file_name):
    """
    Saves the key into a file
    """
    with open(file_name, "wb") as key_file:
        key_file.write(key)

def load_key(file_name):
    """
    Loads the key from the specified file
    """
    return open(file_name, "rb").read()

def encrypt_file(file_name, key):
    """
    Encrypts a file using the specified key
    """
    f = Fernet(key)
    with open(file_name, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(file_name, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(file_name, key):
    """
    Decrypts a file using the specified key
    """
    f = Fernet(key)
    with open(file_name, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(file_name, "wb") as file:
        file.write(decrypted_data)


"""
Tests  , you can remove them

"""

key = generate_key()
message = "Hello, world!"
encrypted_message = encrypt_message(message, key)
decrypted_message = decrypt_message(encrypted_message, key)
print("Original message:", message)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)

print("########################")

file_name = "my_file.txt"
key_file_name = "my_key.key"
write_key(key,key_file_name)
key = load_key(key_file_name)
with open(file_name, "w") as file:
    file.write("Hello, world!")
encrypt_file(file_name, key)
with open(file_name, "r") as file:
    print("Encrypted file contents:", file.read())
decrypt_file(file_name, key)
with open(file_name, "r") as file:
    print("Decrypted file contents:", file.read())

