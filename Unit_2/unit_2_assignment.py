# PART 1
import numpy as np  # To import np.pi
import random  # To create random samples for calculating circumference.

# Using numpy.pi for simplicity and improved accuracy
def print_circum(radius):
    """Return the circumference of a circle based on provided radius.
    
    Args:
        radius: A number representing the radius of the circle.

    Returns:
        The circumference of the circle.

    """
    return 2 * np.pi * radius
    # Following the assignment directions precisely (MVP):
    # return 2 * 3.14159 * radius

# EXPLANATION:
# This function accepts a parameter representing the radius of the circle, using the accepted formula of 2πr.
# Rather than calculating the circumference using 2 * 3.14159 * radius, I opted to use NumPy's representation of pi, seeing as it represents rounding
# to 15 decimal places as opposed to 5, and creates more human-readable code. By multiplying 2 by pi by the provided radius, we can calculate the circumference
# of the circle. Rather than using a print statement for the function, I opted to simply return the value calculated. This creates code that is expandable;
# any value calculated by this function can then be easily fed into other features. However, as a result, when calling the function, I am required to use a print statement
# to output the value to the terminal.

print("PART 1")
# Using random.sample to generate 3 random integers between 1 and 100.
for r in random.sample(range(1,100), 3):
    print(f"Radius: {r}")  # Print the radius used
    print(f"Circumference: {print_circum(r)}")  # Print the circumference based on calculations by print_circum().


#########################################################################################################################################################################
# PART 2
from itertools import combinations  # Normally I would include this with the other imports in part 1, but I wanted to have a clear separation between the two parts. This will help create the various combinations of items. 

# Storing the list of items and their values in a dictionary, as dictionaries are generally faster to access than arrays.
catalog = {"Item 1": 200.00,
          "Item 2": 400.00,
          "Item 3": 600.00}

# Using list comprehension to create possible combinations using the items specified as keys in the catalog dictionary.
combos = [combo for i in range(2, len(catalog) + 1) for combo in combinations(catalog.items(), i)]
phone_num = '98764678899'  # Organization phone number to call for delivery, as specified in the sample output

# Setting up visual structure of the output.
print() # Create a new line for additional visual separation between parts 1 and 2.
print("PART 2")
print('Online Store')
print('-' * 46)  # Creates 46 hyphens
print("Product(s)" + " " * 29 + "Price")  # Structures the Product(s) and Price label, in addition to the spaces in-between

# Print the items and prices stored in our catalog dictionary
for k,v in catalog.items():
    print(k + ' ' * 33 + f"${v:.2f}")  # Print statement includes 33 spaces. Utilizing f-strings to add a dollar sign, and using the .2f format specifier to display 2 digits after decimal for cents

combo_idx = 1  # Setting as an index for the number of combinations created; this will be used in the print statements for the combos
# For each combination created by our list comprehension:
for combo in combos:
    names = [i[0] for i in combo]  # Extract the names of the items.
    prices = sum(i[1] for i in combo)  # Extract the sum of the prices of the items in the combination.

    # If there are two items in the combo (utilizing a set to verify they are unique items):
    if len(set(combo)) == 2:
        discount = prices * 0.10  # Calculate what 10% of the price would be
    # If there are three or more items in the combo (utilizing a set to verify they are unique items):
    elif len(set(combo)) <= 3:
        discount = prices * 0.25  # Calculate what 25% of the price would be
    else:
        discount = 0  # No discount if neither condition is met

    discounted_price = prices - discount  # Subtract discount from original price
    if combo_idx <= 3:
        # If this is combo 1, 2, or 3, print the combination description and price
        print(f"Combo {combo_idx} ({', '.join(names)}) {" " * 13} ${discounted_price:.2f}")
    else:
        # If this is past combo 3, print the combination description and price with fewer spaces for visual cleanliness due to having more characters
        print(f"Combo {combo_idx} ({', '.join(names)}) {" " * 5} ${discounted_price:.2f}")
    combo_idx += 1

print('_' * 46)  # For visual structure
print(f"For Delivery Contact: {phone_num}")  # Print the phone number specified above.

# EXPLANATION:
# For this section, I initially set up the visual structure for the output as shown in the sample output provided, including 'Online Store', and labels for Product(s) and Prices,
# using spaces to separate the labels. I created a catalog using a dictionary, containing the product names as keys and their prices as values. 
# Then, using list comprehension, I created an array of the possible product combinations, such as Item 1 + Item 2, Item 2 + Item 3, and Item 1 + Item 2 + Item 3.
# This helps with expandability of the code, requiring less changes to add more products in the future. I then printed the key and value for each item contained in the catalog,
# utilizing spaces to ensure the values fall in the correct place under the label. Using a for loop, I extracted the names of the items contained in each combination as
# defined in the array previously created. I did the same to calculate the sums of the prices contained in each combo. I created an if statement to check if there are 2 unique items
# in the combo, as verified using a set. If there are, I calculated what 10% of the price would be. The same was done for three or more items in the combo, calculating what 25% of the price
# would be. I then calculated the discounted total price, whether it was 0%, 10%, or 25% off. This was then included in print statements containing the combination number, description, and adjusted price.
# Because combinations of 3 or more items require more characters to describe the combination, I created combo_idx  as a variable to track which combination number is being printed at that time,
# increasing its value by 1 after each iteration through the for loop. By doing this, I was able to define combination numbers (ex: Combo 1, Combo 2, Combo 3) in my print statements, 
# and adjust the number of spaces being included in the print statement to ensure visual cleanliness.


# This approach illustrates several key features of Python:
# Dicionary handling; showcasing the ability to easily store and retrieve data using key-value pairs.
# Combinatorics: Using itertools.combinations shows how powerful Python's capabilities are for generating subsets of collections.
    # It also helps dynamically generate all combinations without the need to manually specify then. This helps keep the code flexible.
# List Comprehension: The use of list comprehension helps illustrate Python's capability to write clean and expressive code, creating the list in a single line
    # and efficiently generating all relevant combinations.
# Looping / Data Extraction: The for loop used extracted item names and prices, and illustrates Python's concise syntax for processing collections.
# Mathematical calculations & Conditional logic: The use of conditional logic to apply different discount rates based on the number of unique items in a combination
    # and dynamically calculate the discount and final price dynamically helps illustrate Python's strengths in numerical calculations.
# String Manipulation: String joining as demonstrated in lines 77 and 79, in addition to the use of f-strings illustrate the ability to create user-friendly outputs
    # Additionally, the use of f-strings helps make formatting of financial values with two decimal places easily readable.
# Modularity and Scalability: The ability for discount rates to be easily modified and the catalog to be easily expanded help illustrate Python's adaptability to changing
    # business requirements.