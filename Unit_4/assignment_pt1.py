# Step 1: create a basic skeleton for our function. Function is defined with
# two parameters 'a' and 'b', representing the lengths of the two legs
# of the right triangle. We will go ahead and return 0 to ensure the function
# is returning a defined value as anticipated.
# def calc_hypotenuse(a, b):
#     return 0
# print(calc_hypotenuse(1,2))  # Test input; Output: 0

# Step 2: implement the hypotenuse formula (c=sqrt(a^2+b^2)); import numpy 
# to use the sqrt function. Use print statements to ensure calculations are as expected at each stage. Our return statement
# can be assumed to represent c due to the sole purpose of the function being calculating the
# hypotenuse. Justification for using NumPy over the math library: numpy was chosen due to it generally being a bit faster than math; 
# while these calculations are simple enough that it doesn't make a real difference, it is still a good habit. Not 
# to mention, many other popular Python libraries (such as pandas) need numpy to be used as opposed to math.
# import numpy as np
# def calc_hypotenuse(a, b):
#     # Expected Output: a^2 = 9; b^2 = 16 
#     print(f'a^2 = {a**2}; b^2 = {b**2}')  # Actual Output (Using input shown below): a^2 = 9; b^2 = 16
#     # Expected Output (Using input shown below): a^2 + b^2 = 25
#     print(f'a^2 + b^2 = {a**2 + b**2}')  # Actual Output (Using input shown below): a^2 + b^2 = 25
#     return np.sqrt(a**2 + b**2)

# # Test input; expected output: 5
# print(calc_hypotenuse(3, 4))  # Output: 5.0

# Step 3: Now that we know each stage of our calculations are working as anticipated, we can remove the print statements.
# We will then test the function with known values, and compare the actual output with the output we are expecting.
# import numpy as np
# def calc_hypotenuse(a, b): 
#     return np.sqrt(a**2 + b**2)

# print(calc_hypotenuse(3, 4))  # Expected Output: c = 5; Actual Output: 5.0
# print(calc_hypotenuse(3, 8))  # Expected Output: c ≈ 8.544; Actual Output: 8.54400374531753
# print(calc_hypotenuse(20, 40))  # Expected Output: c ≈ 44.72; Actual Output: 44.721359549995796

# Step 4: Create docstrings for the function; while normally docstrings would be created earlier in this process to document
# for collaboration with other developers, an argument can be made that this function is simple enough to justify 
# creating docstrings at any point before pushing changes to a shared development or production build.
import numpy as np
def calc_hypotenuse(a, b):
    """
    Calculate the length of the hypotenuse of a right triangle.

    Given the lengths of the two legs (a and b) of a right triangle, 
    this function computes the length of the hypotenuse using the 
    Pythagorean theorem: c = sqrt(a^2 + b^2), where:
        - a: Length of one leg of the triangle.
        - b: Length of the other leg of the triangle.

    Parameters:
    a (float or int): Length of the first leg of the triangle.
    b (float or int): Length of the second leg of the triangle.

    Returns:
    float: The length of the hypotenuse.

    Example:
    >>> calc_hypotenuse(3, 4)
    5.0

    Note:
    The function assumes that the input values are non-negative.
    """ 
    return np.sqrt(a**2 + b**2)

print(calc_hypotenuse(3, 4))  # Expected Output: c = 5; Actual Output: 5.0
print(calc_hypotenuse(3, 8))  # Expected Output: c ≈ 8.544; Actual Output: 8.54400374531753
print(calc_hypotenuse(20, 40))  # Expected Output: c ≈ 44.72; Actual Output: 44.721359549995796
