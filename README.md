# Instagram Story Liker

This Python script enables you to automatically like stories on Instagram for a list of specified usernames.

## Overview

The Instagram Story Liker script offers the following functionalities:

- **Login**: Automatically logs in to your Instagram account using the provided credentials or prompts you to enter them if not saved.
- **Like Stories**: Scans the stories of specified usernames and likes them if available.
- N**otification Handling**: Handles situations where stories are not available or have already been liked.

## Requirements

- Python 3.x
- Selenium
- ChromeDriver
- Webdriver Manager

## Setup Instructions

1. Install Python 3.x.
2. Install required Python packages using pip: `pip install selenium webdriver-manager`
3. Download and install ChromeDriver according to your Chrome browser version.
4. Create a text file named `followers.txt` containing the list of usernames whose stories you want to like, with each username on a new line.
5. Run the script by executing the `instagram_story_liker.py` file.

## How to Use

- Run the script by executing python instagram_story_liker.py.
- Log in to your Instagram account when prompted or provide the credentials in the credentials.txt file.
- The script will scan the stories of the specified usernames and like them if available.
- Check the console output for status updates and notifications.

## Note

- This script is for educational purposes only and should be used responsibly.
- Ensure you have a stable internet connection while running the script.

## License

This project is licensed under the MIT License.

Author
