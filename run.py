import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException


def save_credentials(username, password):
    with open("credentials.txt", "w") as file:
        file.write(f"{username}\n{password}")


def load_credentials():
    if not os.path.exists("credentials.txt"):
        return None

    with open("credentials.txt", "r") as file:
        lines = file.readlines()
        if len(lines) >= 2:
            return lines[0].strip(), lines[1].strip()

    return None


def prompt_credentials():
    username = input("Enter your Instagram username: ")
    password = input("Enter your Instagram password: ")
    save_credentials(username, password)
    return username, password


def read_usernames_from_file(file_path):
    with open(file_path, "r") as file:
        usernames = [line.strip() for line in file]
    return usernames


def check_logged_in(driver):
    try:
        # Look for a specific element that indicates the user is logged in
        driver.find_element(By.XPATH, "//span[text()='Home']")
        print("Logged In Successfully!")
        return True
    except NoSuchElementException:
        print("!!! NOT Logged In !!!")
        return False


def login(driver, username, password):
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(2)

    username_input = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
    password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")

    username_input.send_keys(username)
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)


def like_stories(username, password, usernames):
    # Set up ChromeDriver options
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Set up ChromeDriver service
    service = Service(ChromeDriverManager().install())

    # Set up ChromeDriver instance
    driver = webdriver.Chrome(service=service, options=chrome_options)

    logged_in = check_logged_in(driver)

    if not logged_in:
        credentials = load_credentials()
        if credentials is None:
            login(driver, username, password)
            save_credentials(username, password)
        else:
            username, password = credentials
            login(driver, username, password)

    logged_in = check_logged_in(driver)

    # Like Stories Logic by @mateo1mc
    for follower in usernames:
        story_url = f"https://www.instagram.com/stories/{follower}"
        driver.get(story_url)
        time.sleep(2)

        view_story_xpath = '//div[@role="button"][.="View Story"]'
        like_button_xpath = '//div[@role="button"][contains(.,"Like")]'
        next_button_xpath = '//div[@role="button"][contains(.,"Next")]'
        notification_tab__xpath = '//span[contains(.,"Turn on notifications")]'
        # home_button_xpath = '//span[text()="Home"]' # if notification_tab__xpath does not work

        try:
            # Check if the "View Story" button exists
            view_story_button = driver.find_element(By.XPATH, view_story_xpath)
            print("[TRUE] --> " + follower + " has updated the story.")
            view_story_button.click()
            time.sleep(2)
            
            # Loop to Like each Story
            while True:
                try:
                    # Click the "Like" button
                    like_button = driver.find_element(By.XPATH, like_button_xpath)
                    like_button.click()
                    print("You Liked " + follower + "'s Story Successfully!")
                    time.sleep(2)
                except NoSuchElementException:
                    print("This story was Liked before!")

                try:
                    # Click the "Next" button
                    next_button = driver.find_element(By.XPATH, next_button_xpath)
                    next_button.click()
                    print("Next Story!")
                    time.sleep(2)
                except NoSuchElementException:
                    print("Next button not found.")

                try:
                    # Check if No more Stories and Exit the loop
                    home_button = driver.find_element(By.XPATH, notification_tab__xpath)
                    print("No more Stories for " + follower)
                    break
                except NoSuchElementException:
                    print(15 * "-")

        except NoSuchElementException:
            print("[FALSE] --> " + follower + " has not uploaded any story recently!")

