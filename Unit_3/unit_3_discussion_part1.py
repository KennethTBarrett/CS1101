# CHAINED VS NESTED CONDITIONALS:
# A chained conditional uses a sequence of if-elif-else statements to evaluate multiple conditions
# in a specified order from top to bottom, with each statement providing a new condition to evaluate
# if the previous conditions were not true. On the other hand, a nested conditional is essentially a conditional
# statement inside of another conditional. This means that 

# Chained conditional.
def what_generation(age):
    '''Accepts an age, and returns the person's generation based on currently accepted boundaries.'''
    if age < 12:
        return "Gen Alpha"
    elif 12 <= age <= 27:
        return "Gen Z"
    elif age <= 43:
        return "Millenial"
    elif age <= 59:
        return "Gen X"
    elif age <= 78:
        return "Baby Boomer"
    elif age <= 96:
        return "Post-War"
    elif age <= 102:
        return "WWII"
    else:
        # For simplification; not handling invalid values
        return "Unknown Generation"

# Example usage:
print(what_generation(28))  # Millenial
print(what_generation(67))  # Baby Boomer
print(what_generation(115))  # Unknown Generation

# Nested conditional.
def generation_iq(age, iq):
    '''Accepts an age and IQ score, and returns the person's generation
       based on currently accepted boundaries and level of intelligence
       based on IQ according to KABC-II 2004 Descriptive Categories'''
    if age < 12:
        generation = "Gen Alpha"
    elif 12 <= age <= 27:
        generation = "Gen Z"
    elif age <= 43:
        generation = "Millenial"
    elif age <= 59:
        generation = "Gen X"
    elif age <= 78:
        generation = "Baby Boomer"
    elif age <= 96:
        generation = "Post-War"
    elif age <= 102:
        generation = "WWII"
    else:
        generation = "Unknown Generation"

    # Return both the generation and intelligence
    return f"Generation: {generation}, Intelligence: {intelligence}"



# Example usage:
print(generation_iq(25, 130))  # Gen Z, Above Average IQ
print(generation_iq(50, 131))  # Gen X, Upper Extreme
print(generation_iq(70, 90))   # Baby Boomer, Average IQ
