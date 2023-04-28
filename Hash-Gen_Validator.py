import os
import hashlib
from tkinter import filedialog
from tkinter import Tk

# Create a Tkinter root window
root = Tk()
root.withdraw()

def get_file_path():
    """Prompt user to select a file and return its path"""
    return filedialog.askopenfilename()

def get_text():
    """Prompt user to enter text and return it"""
    return input('Enter text: ')

def get_content():
    """Prompt user to select a file or enter text and return its content"""
    while True:
        choice = input('Select content:\n1. File\n2. Text\nEnter your choice: ')
        if choice == '1':
            file_path = get_file_path()
            if os.path.exists(file_path):
                with open(file_path, 'rb') as file:
                    return file.read()
            else:
                print('File does not exist. Please try again.')
        elif choice == '2':
            return bytes(get_text(), 'utf-8')
        else:
            print('Invalid choice. Please try again.')

# Define a dictionary of hash algorithms
hash_algorithms = {
    'MD5': hashlib.md5,
    'SHA-1': hashlib.sha1,
    'SHA-224': hashlib.sha224,
    'SHA-256': hashlib.sha256,
    'SHA-384': hashlib.sha384,
    'SHA-512': hashlib.sha512,
    'SHA3-224': hashlib.sha3_224,
    'SHA3-256': hashlib.sha3_256,
    'SHA3-384': hashlib.sha3_384,
    'SHA3-512': hashlib.sha3_512,
    'BLAKE2b': hashlib.blake2b,
    'BLAKE2s': hashlib.blake2s,
    'SHAKE128': hashlib.shake_128,
    'SHAKE256': hashlib.shake_256,
}

# Prompt the user to select a hash algorithm
print('Select a hash algorithm:')
for i, algorithm in enumerate(hash_algorithms.keys()):
    print(f'{i + 1}. {algorithm}')
while True:
    try:
        choice = int(input('Enter your choice: '))
        if choice in range(1, len(hash_algorithms) + 1):
            break
        else:
            print('Invalid choice. Please enter a number between 1 and', len(hash_algorithms))
    except ValueError:
        print('Invalid input. Please enter a number.')

# Get the selected hash algorithm
algorithm_name = list(hash_algorithms.keys())[choice - 1]
algorithm = hash_algorithms[algorithm_name]

# Check if the file or text exists
content = get_content()

# Calculate the hash value of the file or text contents
hash_value = algorithm(content).hexdigest()

# Print the hash value
print(f"{algorithm_name} hash value of the file or text:", hash_value)

# Prompt the user to enter a known hash value for verification or select a new file or text
while True:
    choice = input('Select an option:\n1. Verify hash value\n2. Pick new file or text\n3. Exit\nEnter your choice: ')
    if choice == '1':
        known_hash_value = input('Enter the known hash value for verification: ')
        if known_hash_value == hash_value:
            print('Hash value verified: the file or text has not been tampered with.')
        else:
            print('Hash value verification failed: the file or text may have been tampered with.')
    elif choice == '2':
        content = get_content()
        hash_value = algorithm(content).hexdigest()
        print(f"{algorithm_name} hash value of the new file or text:", hash_value)
    elif choice == '3':
        break
    else:
        print('Invalid choice. Please try again.')
