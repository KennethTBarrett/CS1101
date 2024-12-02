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
    elif 28 <= age <= 43:
        return "Millenial"
    elif 44 <= age <= 59:
        return "Gen X"
    elif 60 <= age <= 78:
        return "Baby Boomer"
    elif 79 <= age <= 96:
        return "Post-War"
    elif 97 <= age <= 102:
        return "WWII"
    else:
        # For simplification; not handling invalid values
        return "Unknown Generation"

# Example usage:
print(what_generation(28))  # Millenial
print(what_generation(67))  # Baby Boomer
print(what_generation(115))  # Unknown Generation

# Nested conditional.
def generation_part(age):
    if age < 12:
        generation = "Gen Alpha"
        if age <= 6:
            part_of_gen = "Younger End"
        else:
            part_of_gen = "Older End"
    elif 12 <= age <= 27:
        generation = "Gen Z"
        if age <= 20:
            part_of_gen = "Younger End"
        else:
            part_of_gen = "Older End"
    elif 28 <= age <= 43:
        generation = "Millenial"
        if age <= 35:
            part_of_gen = "Younger End"
        else:
            part_of_gen = "Older End"
    elif 44 <= age <= 59:
        generation = "Gen X"
        if age <= 51:
            part_of_gen = "Younger End"
        else:
            part_of_gen = "Older End"
    elif 60 <= age <= 78:
        generation = "Baby Boomer"
        if age <= 69:
            part_of_gen = "Younger End"
        else:
            part_of_gen = "Older End"
    elif 79 <= age <= 96:
        generation = "Post-War"
        if age <= 85:
            part_of_gen = "Younger End"
        else:
            part_of_gen = "Older End"
    elif 97 <= age <= 102:
        generation = "WWII"
        if age <= 99:
            part_of_gen = "Younger End"
        else:
            part_of_gen = "Older End"
    else:
        generation = "Unknown Generation"
        part_of_gen = "Unknown End"
    # Using .lower() because I changed my mind on how I wanted this to print.
    return f"{age} is on the {part_of_gen.lower()} of the generation: {generation}"



# Example usage:
print(generation_part(25))  # 25 is on the older end of the generation: Gen Z
print(generation_part(50))  # 50 is on the younger end of the generation: Gen X
print(generation_part(70))  # 70 is on the older end of the generation: Baby Boomer