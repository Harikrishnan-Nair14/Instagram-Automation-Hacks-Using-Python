# Follow Harikrishnan-Nair14 for more Programming Related Concepts...Life is Coding...
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import time

# Configuration
instagram_url = "https://www.instagram.com"
username = "YOUR_USERNAME"
password = "YOUR_PASSWORD"
post_url = "YOUR_INSTAGRAM_LINK"  # Replace with the actual post URL
comment_text = "Jay Shree Ram...Krishna is Happiness"

# Path to chromedriver executable
chromedriver_path = r"C:\Users\Harikrishnan Nair\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe" # Place your Chromedriver URL after Extraction

# Initialize the WebDriver using the Service object
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

try:
    # Open Instagram and log in
    driver.get(instagram_url)
    time.sleep(3)  # Wait for the page to load

    # Enter username
    username_input = driver.find_element(By.NAME, 'username')
    username_input.send_keys(username)

    # Enter password
    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys(password)

    # Submit login form
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)  # Wait for login to complete

    # Navigate to the post
    driver.get(post_url)
    time.sleep(3)  # Wait for the post to load

    # Find the comment box and enter the comment
    while True:
        try:
            comment_box = driver.find_element(By.CSS_SELECTOR, 'textarea[placeholder="Add a comment…"]')
            comment_box.click()
            comment_box.send_keys(comment_text)

            # Post the comment
            comment_box.send_keys(Keys.RETURN)
            break  # Exit the loop if successful
        except StaleElementReferenceException:
            time.sleep(1)  # Wait a bit before trying again
        except NoSuchElementException:
            time.sleep(1)  # Wait a bit before trying again

    time.sleep(3)  # Wait for the comment to be posted

finally:
    # Close the WebDriver
    driver.quit()
