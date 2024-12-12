# Section 6.9 Debugging of your textbook lists three possibilities to consider if a function is not working.
# · Describe each possibility in your own words.
# · Define "precondition" and "postcondition" as part of your description.
# · Create your own example of each possibility in Python code. List the code for each example, along with sample output from trying to run it.

# Precondition violation:
# A precondition is a requirement that must be true before a function is called for it to operate as expected. If parameters are missing, or
# if values passed as arguments are out of range or an invalid datatype, the function will not execute as intended. In the example I provided,
# the function requires a valid image file to convert to a URI string. If the file passed into the function does not exist or is not a valid image file,
# these preconditions have not been met, leading to a postcondition violation

# Postcondition violation:
# A postcondition is a condition that must be true after the function completes execution. If the function doesn't produce the expected result / has flawed logic,
# this is considered a postcondition violation. In the example I provided, the logic is faulty; even though the function correctly encodes the file and produces
# a string, for the URI string to be valid,  it requires the prefix "data:image/png;base64,". Because of this, the result produced by the function is not valid,
# demonstrating not only an example of a postcondition violation but also the importance of attention to detail regarding technical requirements.

# Return violation:
# A return violation occurs when a function behaves correctly, but its return value is misrepresented or used incorrectly. It may even refer to a function that
# should return a value but doesn't. In the example I provided, the function returns the correct value as a string, but in the usage example shown, the return value is treated like a file object using the close() method.

import base64
import os

def precondition(image_path):
    # Check the precondition; the file must exist...
    if not os.path.isfile(image_path):
        raise ValueError(f"Precondition violated: the file '{image_path}' does not exist.")
    # ... and be an image.
    if not image_path.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
        raise ValueError(f"Precondition violated: '{image_path}' is not a valid image file (.png, .jpg, .jpeg, .gif)")
    with open(image_path, "rb") as image_file:
        return "data:image/png;base64," + base64.b64encode(image_file.read()).decode("utf-8") 

def postcondition(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")
    except FileNotFoundError:
        raise ValueError("Image file not found")
    
def return_issue(image_path):
    with open(image_path, "rb") as image_file:
        return "data:image/png;base64," + base64.b64encode(image_file.read()).decode("utf-8") 

invalid_image = 'image.txt'
valid_image = 'image.png'

# PRECONDITION VIOLATION
print('=' * 100), print("Precondition Violation:")  # Formatting
try:
    uri = precondition(invalid_image)
    print(uri)
except ValueError as e:
    print(f"Error: {e}")


# POSTCONDITION VIOLATION
print('=' * 100), print("Postcondition Violation:")  # Formatting
try:
    uri = postcondition(valid_image) 
    if not uri.startswith("data:image/"):
        raise ValueError("Postcondition violated: The URI is not valid.")
    print(uri)
except ValueError as e:
    print(f"Error: {e}")

# RETURN VIOLATION
print('=' * 100), print("Return Violation:")  # Formatting
try:
    uri = return_issue(valid_image)
    # Mistakenly treating return value as a file object.
    uri.close()  # Will raise an attribute error because 'uri' is a string.
except AttributeError as e:
    print(f"Error: {e}")
print('=' * 100)  # Formatting