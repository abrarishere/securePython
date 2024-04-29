    """
    Encrypts the given text using ASCII-based encryption with a specified key.

    Args:
        text (str): The text to encrypt.
        key (int): The encryption key.

    Returns:
        str: The encrypted text.
    """
    if not isinstance(text, str):
        raise TypeError("{} should be a type string".format(text))
    if not isinstance(key, int):
        raise TypeError("{} should be of type int".format(key))
    return "".join([chr(ord(something) + key) for something in text])


def decrypt(text, key=0):
    """
    Decrypts the given text using ASCII-based decryption with a specified key.

    Args:
        text (str): The text to decrypt.
        key (int): The decryption key.

    Returns:
        str: The decrypted text.
    """
    if not isinstance(text, str):
        raise TypeError("{} should be a type string".format(text))
    if not isinstance(key, int):
        raise TypeError("{} should be of type int".format(key))
    return "".join([chr(ord(something) - key) for something in text])


def main():
    """
    Main function to handle input and output file names.
    """
    try:
        # Ask for the input file name
        input_file_name = input("Enter the input file name: ")
        with open(input_file_name, 'r') as input_file:
            text = input_file.read()

        # Ask whether to encrypt or decrypt
        action = input("Do you want to encrypt (e) or decrypt (d)? ")

        if action == 'e':
            # Ask for the encryption key
            key = int(input("Enter the encryption key: "))
            # Encrypt the text
            result_text = encrypt(text, key)
            output_file_name = 'encrypt.txt'
        elif action == 'd':
            # Ask for the decryption key
            key = int(input("Enter the decryption key: "))
            # Decrypt the text
            result_text = decrypt(text, key)
            output_file_name = 'decrypt.txt'
        else:
            print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
            return

        # Write the result text to the output file
        with open(output_file_name, 'w') as output_file:
            output_file.write(result_text)

        print("Operation successful.")

    except FileNotFoundError:
        print("File not found!")
    except ValueError:
        print("Invalid key. Please enter an integer.")


if __name__ == "__main__":
    main()
