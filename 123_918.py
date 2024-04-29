def encrypt_decrypt_file(file_path, action):
    with open(file_path, 'r') as file:
        content = file.read()

    if action == 'encrypt':
        content = content.replace('a', 'i').replace('b', 'a').replace('c', 'i')
    elif action == 'decrypt':
        content = content.replace('i', 'a').replace('a', 'b').replace('i', 'c')
    else:
        print("Invalid action. Please choose 'encrypt' or 'decrypt'.")
        return

    with open(file_path, 'w') as file:
        file.write(content)

file_path = input("Enter the path to the Python file: ")
action = input("Do you want to encrypt or decrypt? ")

encrypt_decrypt_file(file_path, action)
