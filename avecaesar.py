import string


def caesar(text, key):
    # Convert text to uppercase and remove non-alphanumeric characters
    text = ''.join(i for i in text.upper() if i.isalnum())

    # Initialize an empty string to store the encrypted text
    new_text = ''

    # Iterate over each character in the cleaned text
    for i in text:
        # Check if the character is alphabetic
        if i.isalpha():
            # Calculate the shifted index using the key
            shifted_index = (string.ascii_uppercase.index(i) + key) % 26

            # Append the corresponding character from the uppercase alphabet to the new_text
            new_text += string.ascii_uppercase[shifted_index]
        else:
            # If the character is not alphabetic, append it directly to new_text
            new_text += i

            # Return the encrypted text
    return new_text
