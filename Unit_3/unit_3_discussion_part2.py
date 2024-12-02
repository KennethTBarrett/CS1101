# This code is intended to reflect a use case for data scientists.
import pandas as pd

# Deeply Nested Conditional (Hard to Read)
def load_dataset_old(file_path):
    if file_path.endswith(".csv"):
        try:
            data = pd.read_csv(file_path)
            return data
        except Exception as e:
            raise ValueError(f"Error reading CSV file: {e}")
    else:
        if file_path.endswith(".xls") or file_path.endswith(".xlsx"):
            try:
                data = pd.read_excel(file_path)
                return data
            except Exception as e:
                raise ValueError(f"Error reading Excel file: {e}")
        else:
            raise ValueError("Unsupported file type")

# Improved Equivalent Conditional (Easier to Read)
def load_dataset_new(file_path):
    try:
        if file_path.endswith(".csv"):
            return pd.read_csv(file_path)
        elif file_path.endswith(".xls") or file_path.endswith(".xlsx"):
            return pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file type")
    except Exception as e:
        raise ValueError(f"Error loading file: {e}")

# Flatten the logic
# By using if-elif-else control flow statements, we can reduce or eliminate unnecessary nesting in our code. The el-if-else construct enables us to write clear,
# sequential checks for various conditions without requiring excessive indentation. By avoiding unnecessary nesting, the code has a more linear, top-down flow that
# makes it easier to follow and debug, improving not only readability but team productivity when working in a collaborative environment... 
# Not to mention that deeply nested and convoluted logic is a recipe for introducing new bugs. 

# Use only one error handling block
# By consolidating the try-except block, we can handle all exceptions uniformly. This makes the code cleaner and easier to read, while also reducing redundancy; 
# when error handling is scattered, the risk of unintentional duplication rises. Redundancy quickly clutters up the code, making it much more difficult to read and understand.

# Utilize early returns
# In this example, each file type is checked, and the function returns immediately when a match is found, preventing further execution when unnecessary.
# This helps improve both the efficiency and clarity of our code. Additionally, by immediately returning a matched case, we can avoid redundant evaluations
# and maintain a clear and logical flow. It's also worth mentioning that this strategy contributes to improved performance, since
# the function stops processing once the relevant condition is met. This is why I started with .csv files, as they are one of the most common file formats used by data scientists (see use case for this script).