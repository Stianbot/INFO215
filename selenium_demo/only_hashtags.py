from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import random

'''
This program is an example of how to search for a Twitter page based on a hashtag -> get new hashtags from the visited
page, except the hashtags that are equal to the original hashtag.
'''

# Initialize the driver.
driver = webdriver.Firefox()

# Function that searches a hashtag on Twitter and returns a set of urls and name of the hashtags it finds.
# Does not return the hashtag that is originally searched for.
def find_hashtag(hashtag):
    # Get Twitter-page based on hashtag.
    url = f'https://twitter.com/hashtag/{hashtag}?src=hashtag_click'
    driver.get(url)

    # Driver wait until at least one hashtag appears.
    WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located(
            (By.PARTIAL_LINK_TEXT, "#")))

    # Gets all 'a' tags from the page.
    a = driver.find_elements_by_tag_name('a')

    # Makes a part of a regex expression based on the hashtag used for the original search.
    # Will be used to exclude links containing the original hashtag.
    # Makes it in lower, upper and capitalized form.
    blacklist = f"(?!{hashtag.lower()})(?!{hashtag.upper()})(?!{hashtag.capitalize()})"

    # Compiles rest of the regular expression.
    full = f"(https:\/\/twitter\.com\/hashtag\/){blacklist}.*=hashtag_click"
    regex = re.compile(full)

    # Empty list where results are appended.
    result = []

    for link in a:

        # Gets url from the a-tags.
        url = link.get_attribute('href')

        # Gets text value of a-tags.
        hashtag_text = link.get_attribute('text')

        # Checks if url matches with regular expression made on line 37-38.
        if regex.match(url) is not None:
            # Adds url(to hashtag) and hashtag text as list.
            result.append([url, hashtag_text])



    return result


# Calls on the created function.
tags = find_hashtag("Bergen")


# Prints results from search: "Bergen" (line 62)
for stuff in tags:
    print(f"Hashtag: {stuff[1]}, Hashtag-url: {stuff[0]}")


# Close the driver - this closes the web browser window.
driver.quit()

'''
This program can be improved by making it remember all blacklisted hashtags. This can be done with a loop that generates
a new regular expression for every page visited. Combined with the code on line 34 this can easily be done.
'''
