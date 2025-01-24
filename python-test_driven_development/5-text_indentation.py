def text_indentation(text):
    """
    Prints a text with 2 new lines
    after each of these characters: '.', '?', ':'

    Args:
        text (str): The text to process.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Remove unnecessary spaces around the string
    text = text.strip()

    # Define characters after which we add two new lines
    special_chars = ['.', '?', ':']

    # Temporary string to store the processed text
    result = ""
    i = 0

    while i < len(text):
        result += text[i]

        # Check if the character is a special character
        if text[i] in special_chars:
            result += "\n\n"  # Add two new lines

            # Skip any spaces following the special character
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue

        i += 1

    # Print the result without unnecessary blank lines
    print("\n".join([line.strip() for line in result.split("\n")]))
