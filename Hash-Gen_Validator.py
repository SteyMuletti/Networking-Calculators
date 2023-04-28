import os
import hashlib
from tkinter import filedialog
from tkinter import Tk

# Create a Tkinter root window
root = Tk()
root.withdraw()

# Open a file dialog box to select a file
file_path = filedialog.askopenfilename()

# Check if the file exists
if os.path.exists(file_path):

    # Define a list of hash algorithms
    hash_algorithms = {
        'MD5': hashlib.md5,
        'SHA-1': hashlib.sha1,
        'SHA-256': hashlib.sha256,
        'SHA-512': hashlib.sha512
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

    # Open the file and read its contents
    with open(file_path, 'rb') as file:
        content = file.read()

    # Calculate the hash value of the file contents
    hash_value = algorithm(content).hexdigest()

    # Print the hash value
    print(f"{algorithm_name} hash value of the file:", hash_value)

    # Prompt the user to enter a known hash value for verification
    known_hash_value = input('Enter the known hash value for verification: ')

    # Compare the computed hash value with the known hash value
    if known_hash_value == hash_value:
        print('Hash value verified: the file has not been tampered with.')
    else:
        print('Hash value verification failed: the file may have been tampered with.')

else:
    print("File does not exist.")
