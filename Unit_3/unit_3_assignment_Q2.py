def divide():
    '''Asks user to input values for a numerator and denominator
       Throws an exception if the user divides by zero. Formats numbers
       for cleanliness in output regardless if the value is a float or integer.'''
    # Continue to request user input until valid values have been entered.
    while True:
        try:
            # Prompt user to input values for numerator and denominator. Accepting input as float for simplification
            # if user inputs a whole or floating-point number. Fed through format_num for visual cleanliness in print statement.
            num = format_num(float(input("Enter the numerator: ")))
            denom = format_num(float(input("Enter the denominator: ")))

            # If a user attempts to divide by zero, ZeroDivisionError: division by zero will be thrown.
            # As a result, we need to create a condition that will raise an error informing the user that division
            # by zero is not possible. Otherwise, the program will crash. Furthermore, it's important to inform the
            # user of why the error has been thrown and provide actionable information on how to fix it moving forward. 
            # As a result, we will use the following conditional statement, raising a ValueError.
            
            # If the user inputs 0, raise a value error to inform them numbers cannot be divided by zero.
            if denom == 0:
                raise ValueError("Numbers cannot be divided by zero")  # Otherwise output would be: ZeroDivisionError: division by zero
            
            # Perform the division and display the result, using format_num for formatting calculation results.
            print(f"{num} / {denom} = {format_num(num / denom)}")
            break  # Exit the loop after a successful calculation
        
        # Print exception; this one print statement should inform the user what needs to be changed for a successful result.
        # For example, if the value error raised in lines 11-12 applies, the user will be told that "Numbers cannot be divided by zero"
        # since the denominator cannot be 0 in a division calculation. Otherwise, any other value error that could be thrown, such
        # as from entering a non-numerical value as input, will be thrown, again informing the user a valid number for division
        # calculations must be entered. Because we raised a ValueError for dividing by zero, this should help the user understand
        # the cause of the error.
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid number for division as input.")

def format_num(val):
    '''Accepts input; if value is a whole number, returns it as an integer.
       Otherwise, returns the value as it was entered.'''
    if val % 1 == 0:  # Modulo operator returns remainder; if remainder of division by 1 is 0, it's a whole number...
        return int(val)  #... and can be converted to and returned as an integer. This will clean up print statements.
    else:
        return val
    

# Calls the divide() function upon initial execution of the script
if __name__ == "__main__":
    divide()

# WHY ERROR HANDLING IS IMPORTANT:
# Error handling helps ensure software is both robust and user-friendly. By giving instructions,
# the software is more prepared to gracefully handle unexpected or invalid conditions. This can
# help prevent crashes and provide feedback to users on how to guide the software to a valid result.
# In the case of a ZeroDivisionError, the program will crash if it is not handled, potentially leading
# to loss of data, and creating a frustrating user experience. When this error is appropriately handled,
# the user is informed about what went wrong and what they need to do to fix it. Additionally, a division by zero
# error could corrupt calculations in software dealing with financial data, and can even expose internal stack traces or other 
# sensitive information that may result in decreased data and company security. Error handling helps validate inputs before performing 
# operations and can provide alternative actions to fall back on. Aside from the users, error handling helps provide a structured way to log issues. 
# This can make debugging easier and provide a way for developers to track recurring issues when the software is in production.
# To sum it up, error handling is vital for ensuring end users have a positive experience by preventing crashing,
# informing users of errors in a way that is clear and guides them on how to solve them, helps ensure stability and security of the software and the data
# it collects and processes. Lastly, error handling helps facilitate debugging efforts and informs long-term software maintenance.
# (246 words)

# No sources have been provided as this knowledge has been attained through my personal professional experience. In particular, extensive error handling
# was a crucial part of my last development position working in a tax preparation software company where data security and integrity were of critical importance.
# I have personally seen the lack of error handling result in disastrous results for organizations and users alike.

# SAMPLE OUTPUTS:
# DENOMINATOR = 0
# Enter the numerator: 10
# Enter the denominator: 0
# Error: Numbers cannot be divided by zero. Please enter a valid number for division as input.

# NUMERATOR = 0
# Enter the numerator: 0
# Enter the denominator: 5
# 0 / 5 = 0

# NUMERATOR IS NOT A NUMBER
# Enter the numerator: a
# Error: could not convert string to float: 'a'. Please enter a valid number for division as input.

# DENOMINATOR IS NOT A NUMBER
# Enter the numerator: 10
# Enter the denominator: abc
# Error: could not convert string to float: 'abc'. Please enter a valid number for division as input.

# NUMERATOR AND DENOMINATOR ARE BOTH VALID WHOLE NUMBERS
# Enter the numerator: 10
# Enter the denominator: 2
# 10 / 2 = 5

# NUMERATOR AND DENOMINATOR ARE BOTH VALID FLOATING POINT NUMBERS
# Enter the numerator: 10.2
# Enter the denominator: 2.4
# 10.2 / 2.4 = 4.25

# NUMERATOR IS A VALID FLOATING POINT NUMBER; DENOMINATOR IS A VALID WHOLE NUMBER
# Enter the numerator: 10.757
# Enter the denominator: 2
# 10.757 / 2 = 5.3785

# NUMERATOR IS A VALID WHOLE NUMBER; DENOMINATOR IS A VALID FLOATING POINT NUMBER
# Enter the numerator: 1000
# Enter the denominator: 2.575
# 1000 / 2.575 = 388.34951456310677