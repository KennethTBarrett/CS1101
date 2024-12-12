# This function is intended for use by Search Engine Optimization specialists. The meta description of a webpage is recommended
# to remain at or under 155 characters; this function will evaluate whether a provided URL's meta description follows these standards, and
# informs the SEO specialist whether the length needs to be shortened.

# Step 1: Create a basic skeleton for our function; this function will be defined with
# a string representing a URL as a parameter
# def meta_desc_len(url):
#     return None
# Test Input:
# print(meta_desc_check('https://worldofwarcraft.blizzard.com/en-us/'))  # Output: None (as expected)

# Step 2: import requests; fetch the page content of a url. Return the response.
# import requests
# def meta_desc_len(url):
#     response = requests.get(url)
#     return response
# Test Input:
# print(meta_desc_len('https://worldofwarcraft.blizzard.com/en-us/')) # Output: <Response [200]> (as expected)

# Step 3: if the response code is 200 as expected, import BeautifulSoup (will require
# installation; can be installed with pip using `pip install beautifulsoup4`) and parse the HTML content. 
# If the response code is not 200, we will not be able to parse the HTML, so create a condition that
# handles other status codes (it's very unlikely this will be needed but it's still important to handle). 
# import requests
# from bs4 import BeautifulSoup
# def meta_desc_len(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')  # Parse HTML
#         return soup
#     else:
#         return f"Failed to retrieve the webpage. Status code: {response.status_code}"
# # Test Input:
# print(meta_desc_len('https://worldofwarcraft.blizzard.com/en-us/'))  Output (as expected): all HTML code from the webpage -- too large to include here. Full output: https://pastebin.com/XjZ09y5L

# Step 4: Using soup.find(), we can query the HTML to search for specific elements. Because meta descriptions are always stored as <meta name="description">, we can easily
# find the meta description tag of a page if it exists.
# import requests
# from bs4 import BeautifulSoup
# def meta_desc_len(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')  # Parse HTML
#         meta_description = soup.find('meta', attrs={'name': 'description'})  # Query contents to find meta description
#         return meta_description
#     else:
#         return f"Failed to retrieve the webpage. Status code: {response.status_code}"
# # Test Input:
# print(meta_desc_len('https://worldofwarcraft.blizzard.com/en-us/')) # Output (as expected): matching HTML code relative to the query; too large to include here. Full output: https://pastebin.com/TBxySmUJ

# Step 5: If the meta description exists, return its content. If not, inform the user no meta description was found.
# import requests
# from bs4 import BeautifulSoup
# def meta_desc_len(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')  # Parse HTML
#         meta_description = soup.find('meta', attrs={'name': 'description'})  # Query contents to find meta description
#         if meta_description:
#             # If the description meta tag is found...
#             # Return the contents
#             return meta_description.get('content')
#         else:
#             return "Meta description not found."
#     else:
#         return f"Failed to retrieve the webpage. Status code: {response.status_code}"
# # Test Input:
# print(meta_desc_len('https://worldofwarcraft.blizzard.com/en-us/')) # Output: "Join thousands of mighty heroes in Azeroth, a world of magic and limitless adventure." (as expected)

# Step 6: As mentioned, SEO best-practices state that meta descriptions should be under approximately 155 characters. Using the meta description content attained during step 6,
# calculate the number of characters contained. We will also be storing the meta description to be a part of our return statement later, as opposed to it being the return statement itself.
# import requests
# from bs4 import BeautifulSoup
# def meta_desc_len(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')  # Parse HTML
#         meta_description = soup.find('meta', attrs={'name': 'description'})  # Query contents to find meta description
#         if meta_description:
#             # If the description meta tag is found...
#             contents = meta_description.get('content')  # Store the contents from meta description query
#             # Return the number of characters
#             return len(contents)
#         else:
#             return "Meta description not found."
#     else:
#         return f"Failed to retrieve the webpage. Status code: {response.status_code}"
# # Test Input:
# print(meta_desc_len('https://worldofwarcraft.blizzard.com/en-us/')) # Output: 85 (as expected)

# Step 7: Evaluate whether the number of characters contained in the meta description fetched from the webpage is at or under 155 characters. Inform the user either way.
# Additionally, similar to our handling of the text itself in step 6, we will be storing the character length of the meta description as well, as opposed to
# simply returning it. This will be used as part of our return statement later.
# import requests
# from bs4 import BeautifulSoup
# def meta_desc_len(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')  # Parse HTML
#         meta_description = soup.find('meta', attrs={'name': 'description'})  # Query contents to find meta description
#         if meta_description:
#             # If the description meta tag is found...
#             contents = meta_description.get('content')  # Store the contents from meta description query
#             # Return the number of characters
#             contents_len = len(contents)  # Store the meta description length
#             if contents_len <= 155:
#                 return 'Meta description length is under 155 characters and thus within recommendations for SEO best-practices.'
#             else:
#                 'Meta description length is too long. Keep the number of characters at or under 155 to avoid truncation.'
#         else:
#             return "Meta description not found."
#     else:
#         return f"Failed to retrieve the webpage. Status code: {response.status_code}"
# # Test Input:
# print(meta_desc_len('https://worldofwarcraft.blizzard.com/en-us/')) # Output: Meta description length is within recommendations for SEO best-practices. (as expected)

# Step 8: format the return statement to be helpful to the user. We will be using the contents of the meta description, the length, and our evaluation of whether
# SEO best-practices for meta description length have been met, and we will return these to the user in a well-formatted, actionable way.
# import requests
# from bs4 import BeautifulSoup
# def meta_desc_len(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')  # Parse HTML
#         meta_description = soup.find('meta', attrs={'name': 'description'})  # Query contents to find meta description
#         if meta_description:
#             # If the description meta tag is found...
#             contents = meta_description.get('content')  # Store the contents from meta description query
#             # Return the number of characters
#             contents_len = len(contents)  # Store the meta description length
#             if contents_len <= 155:
#                 return f'"{contents}" is {contents_len} characters long. Meta description length is under 155 characters and thus within recommendations for SEO best-practices.'
#             else:
#                 f'"{contents}" is {contents_len} characters long. Meta description length is too long. Keep the number of characters at or under 155 to avoid truncation.'
#         else:
#             return "Meta description not found."
#     else:
#         return f"Failed to retrieve the webpage. Status code: {response.status_code}"
# # Test Input:
# print(meta_desc_len('https://worldofwarcraft.blizzard.com/en-us/')) # Output: "Join thousands of mighty heroes in Azeroth, a world of magic and limitless adventure." is 85 characters long. Meta description length is under 155 characters and thus within recommendations for SEO best-practices.

# Step 9: test the function using several URLs.
import requests
from bs4 import BeautifulSoup
def meta_desc_len(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')  # Parse HTML
        meta_description = soup.find('meta', attrs={'name': 'description'})  # Query contents to find meta description
        if meta_description:
            # If the description meta tag is found...
            contents = meta_description.get('content')  # Store the contents from meta description query
            # Return the number of characters
            contents_len = len(contents)  # Store the meta description length
            if contents_len <= 155:
                return f'"{contents}" is {contents_len} characters long. Meta description length is under 155 characters and thus within recommendations for SEO best-practices.'
            else:
                f'"{contents}" is {contents_len} characters long. Meta description length is too long. Keep the number of characters at or under 155 to avoid truncation.'
        else:
            return "Meta description not found."
    else:
        return f"Failed to retrieve the webpage. Status code: {response.status_code}"
# Test Input:
print(meta_desc_len('https://worldofwarcraft.blizzard.com/en-us/')) # Output as expected: "Join thousands of mighty heroes in Azeroth, a world of magic and limitless adventure." is 85 characters long. Meta description length is under 155 characters and thus within recommendations for SEO best-practices.
print(meta_desc_len('https://uopeople.edu/')) # Output as expected: "University of the People is a tuition-free online university for students from all over the world. Learn more about University of the People!" is 141 characters long. Meta description length is under 155 characters and thus within recommendations for SEO best-practices.
print(meta_desc_len('https://www.tensorflow.org/'))  # "An end-to-end open source machine learning platform for everyone. Discover TensorFlow's flexible ecosystem of tools, libraries and community resources." is 151 characters long. Meta description length is under 155 characters and thus within recommendations for SEO best-practices.