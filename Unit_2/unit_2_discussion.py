# Consider a highly simplified decision tree algorithm as the context for this assignment

# EXAMPLE 1
# This function is meant to illustrate which branch of a
# decision tree should be chosen in a simplified manner

def make_decision(criterion):
    if criterion == 'yes':
        return "Branch A"
    elif criterion == 'no':
        return "Branch B"
    else:
        return "Unknown branch based on provided criterion"
    
# Criterion is the parameter, yes is the argument.

result = make_decision('yes')
print(result)  # Output: Branch A

# EXPLANATION:
# In this function, our parameter is 'criterion', a placeholder or variable defined in the function's signature.
# It acts as an input mechanism for receiving values when the function is being called, and exists only within the local scope of the function.
# On the other hand, 'yes' is the argument being used when calling this function. This is the actual data being passed into the function,
# filling the parameter with the actual value as defined.

# EXAMPLE 2
# Passing a value as an argument; 'no' will be our direct literal value
print(make_decision('no'))  # Output: Branch B

# Passing a variable as an argument. In this example, input_val is our variable, holding 'yes', which is then passed as an argument into the function
input_val = 'yes' 
print(make_decision(input_val)) # Output: Branch A

# Passing an expression as an argument. In this example, we will use .upper()
print(make_decision('maybe'.upper()))  # Output: Unknown branch based on provided criterion

# EXPLANATION:
# In this example, our first print statement represents a direct literal value, whereas the second print statement uses a variable.
# In this print statement, the variable 'input_val' holds the value "yes", which is passed as an argument into the function.
# The third print statement uses an expression; in this print statement, 'maybe'.upper() will dynamically evaluate to "MAYBE", which is then passed as an argument into the funcion.


# EXAMPLE 3
def depth():
    how_deep = "Depth of the decision tree"  # Local variable defined inside function
    return how_deep

# Access the local variable within the function by calling the function
print(depth())  # Output: "Depth of the decision tree"

# Attempt to access local variable outside of the funcion
try:
    print(how_deep)  # Results in a NameError
except NameError as e:
    print(e)  # Output: name 'how_deep' is not defined

# Inside the function, depth exists and can be accessed seeing as it is a local variable defined within the scope of the funcion.
# Becaused depth is local to the function and not globally defined, it results in a NameError when attempting to access it outside of the scope of the function.


# EXAMPLE 4
def classify_branch(node_type):
    # node_type is a parameter that is local to this function
    if node_type == 'root':
        return "Root Node"
    else:
        return "Intermediate Node"
    
print(classify_branch('root'))  # Output: Root Node

# Try to use the parameter ouside of the function
try:
    print(node_type)  # Results in a NameError
except NameError as e:
    print(e)  # Output: name 'node_type' is not defined

# EXPLANATION:
# Within the function, node_type can be accessed as it exists as the function parameter within the scope of the function.
# Because node_type is not defined globally, a NameError is thrown when attempting to access it outside of the function.


# EXAMPLE 5
branch = "global"  # Defining global variable

def decision_path():
    branch = "local" # local variable using same name as global counterpart
    # Print the local variable 'branch'
    print("Inside function:", branch)

# Call the function; local variable is output
decision_path()  # Output: Inside function: local

# Global value will remain unchanged due to the scope of the local variable being within the function
print("Outside function:", branch)  # Output: Outside function: global

# EXPLANATION:
# When accessing 'branch' from within the function, the local variable is returned, shadowing the global variable defined before the function.
# When accessing 'branch' from outside of the function, the value of the global variable is returned because the scope of the local variable 'branch' is confined
# to the scope of the function it is defined in. In addition to the lesson, this example helps illustrate the importance of careful and strategic
# efforts in defining variable names to create effective, clean, expandable, and maintainable code.
