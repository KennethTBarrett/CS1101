def first_n_chars(name, n):
    """
    Extracts the first `n` characters from the given string `name`.

    Args:
        name (str): The input string.
        n (str): The number of characters to extract, entered as a string.
                 It will be converted to an integer.

    Returns:
        str: A substring containing the first `n` characters of `name`,
             or an error message if the input for `n` is invalid.

    Example:
        >>> first_n_chars("Hello, World!", "5")
        'Hello'
        >>> first_n_chars("Hello, World!", "abc")
        'Error: The "n" parameter must be a valid integer.'
    """
    try:
        if not name.strip():
            raise ValueError("The name entered cannot be empty or consist only of spaces.")
        if not n.strip():
            raise ValueError("The number of characters cannot be empty or consist only of spaces.")
        if not n.isdigit():
            raise ValueError("The value for the number of characters to display must be a number.")
        n = int(n)
        if n < 0:
            raise ValueError("The number of characters must be a non-negative integer.")
        return name[:n]
    except ValueError as e:
        return f"Error returning specified number of characters: {e}"

def reverse_name(name, case="default"):
    """
    Reverses the given string `name` and optionally applies a case transformation.

    Args:
        name (str): The input string to reverse.
        case (str, optional): Specifies the case transformation for the reversed string. 
                              Defaults to "default".
                              Options:
                              - "default": No case change.
                              - "upper": Converts to uppercase.
                              - "lower": Converts to lowercase.
                              - "invert": Capitalizes the first character of the newly reversed name.

    Returns:
        str: The reversed string with the specified case transformation,
             or an error message if an invalid case is provided.

    Example:
        >>> reverse_name("Python")
        'nohtyP'
        >>> reverse_name("Python", case="upper")
        'NOHTYP'
        >>> reverse_name("Python", case="invert")
        'Nohtyp'
        >>> reverse_name("Python", case="invalid")
        "Error: Invalid case 'invalid' entered."
    """
    try:
        if not name.strip():
            raise ValueError("The name entered cannot be empty or consist only of spaces.")
        if case.lower() not in ["default", "upper", "lower", "invert"]:
            raise ValueError(f"Invalid case '{case}' entered.")
        if case.lower() == "default":
            return name[::-1]
        elif case.lower() == "upper":
            return name[::-1].upper()
        elif case.lower() == "lower":
            return name[::-1].lower()
        elif case.lower() == "invert":
            # Use join method to handle multiple names (e.g. first, middle, last)
            return " ".join(word.capitalize() for word in name[::-1].split())
    except Exception as e:
        return f"Error reversing name: {e}"

def count_vowels(name):
    """
    Counts the number of vowels in the given string `name`, including conditional handling for 'y'.

    Args:
        name (str): The input string in which vowels are counted.

    Returns:
        int: The count of vowels in `name`.

    Notes:
        - Vowels include 'a', 'e', 'i', 'o', 'u' (case-insensitive).
        - The letter 'y' is considered a vowel if it meets these conditions:
            - It is not preceded or followed by another vowel.
            - It is not at the beginning of the string.

    Example:
        >>> count_vowels("rhythm")
        1
        >>> count_vowels("Beautiful")
        5
        >>> count_vowels("SYZYGY")
        1
    """
    try:
        if not name.strip():
            raise ValueError("The name entered cannot be empty or consist only of spaces.")
        return len([
                    x for i, x in enumerate(name)
                    if x.lower() in "aeiou" or
                    (x.lower() == 'y' and ((i > 0 and name[i - 1].lower() not in "aeiou") and
                    (i == len(name) - 1 or name[i + 1].lower() not in "aeiou")))
                    ])
    except Exception as e:
        return f"Error counting the number of vowels: {e}"


if __name__ == "__main__":
    while True:
        # Input processing
        name = input("Please enter the name you'd like to process: ").strip()
        n = input("Please enter the number of characters you'd like to see (including spaces, if applicable): ").strip()
        print("=" * 60)  # Formatting for ease when reading output.

        #first_n_chars
        FIRST_N_RESULT = first_n_chars(name, n)
        if "Error" in FIRST_N_RESULT:
            print(FIRST_N_RESULT)
        else:
            print(f"First {n} characters in '{name}': {FIRST_N_RESULT}")

        # reverse_name
        REVERSE_RESULT = reverse_name(name)
        if "Error" in REVERSE_RESULT:
            print(REVERSE_RESULT)
        else:
            print(f"'{name}' in reverse (default case): {reverse_name(name)}")
            print(f"'{name}' in reverse (all caps): {reverse_name(name, 'upper')}")
            print(f"'{name}' in reverse (all lowercase): {reverse_name(name, 'lower')}")
            print(f"'{name}' in reverse (invert capitalization): {reverse_name(name, 'invert')}")

        # count_vowels
        COUNT_RESULT = str(count_vowels(name))
        if "Error" in COUNT_RESULT:
            print(COUNT_RESULT)
        else:
            print(f"Number of vowels in '{name}': {COUNT_RESULT}")

        # Ask if the user wants to repeat the process
        while True:
            repeat = input("Would you like to process another name? (yes/no): ").strip().lower()
            if repeat == "yes":
                break
            elif repeat == "no":
                exit()
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
