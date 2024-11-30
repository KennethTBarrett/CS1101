def main():
    while True:  # This ensures the progam continues to ask for input until the user provides a valid integer.
        # Try block attempts to convert the user's input into an integer.
        try:
            value = int(input("Please enter an integer: "))
            break  # Break the loop if the user inputs an integer.
        # If the user inputs a value that is not a valid integer...   
        except ValueError:  # ...Raise a ValueError, using the except block to print an error message.
            print(f"Value entered is not an integer -- please enter a whole number, positive or negative.")
    # Determine which function to call
    if value > 0:
        print(countdown(value))
    elif value < 0:
        print(countup(value))
    elif value == 0:
        print(countdown(value))

        # I opted to use the countdown function based upon a coin-flip; because both the countup and countdown functions
        # have a condition to return 'Blastoff' when n = 0, it doesn't make a difference which function is used. However,
        # given complete control of the code structure, I would simply print 'Blastoff!' in the main() function as shown commented
        # below. This enhances code readability and provides a more complete logical structure of the function,
        # reducing the chance of confusing other developers upon their first glance at the code.
        # print('Blastoff!')

# In both the countup() and countdown() functions, I am using a return statement to return 'Blastoff!' because by using print statements alone,
# the function does not have a defined output after completing all recursive calls, leading to the output including None at the end.
def countup(n):
    if n == 0:
        return 'Blastoff!'
    else:
        print(n)
        return countup(n + 1)  # Recursive call.

def countdown(n):
    if n == 0:
        return 'Blastoff!'
    else:
        print(n)
        return countdown(n - 1) # Recursive call

# Calls the main() function upon initial execution of the script.    
if __name__ == "__main__":
    main()