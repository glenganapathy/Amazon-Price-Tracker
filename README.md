# Amazon Price Tracker

This Python script tracks the price of a specific product on Amazon and sends an email alert when the price drops below a user-defined threshold. It uses Selenium to load the product page dynamically and BeautifulSoup to parse the price details from the HTML.

## Features

- Monitors a specific Amazon product's price.
- Sends an email alert when the price drops below a specified threshold.
- Runs in headless mode using Selenium, so no browser window is opened.
- Extracts product details using BeautifulSoup.

## Requirements

- **Python 3.x**
- `selenium` library
- `beautifulsoup4` library
- `smtplib` (included in Python's standard library)

## Configuration

Update the following variables in the script:

- **`url`**: The Amazon product URL to track.
- **`threshold_price`**: The price threshold for receiving alerts.
- **`email`**: Your Gmail address for sending the alert.
- **`pswrd`**: Your Gmail app password (use an app password if two-factor authentication is enabled).

  ### Gmail Setup:
     - Enable 2-Step Verification on your Gmail account.
     - Generate an App Password for the script to send emails.
     - If you are using any other email provider, please ensure to change the smtp server address and ports accordingly. 



##### Worked on this as part of a module project from Dr. Angela Yu's course on Udemy titled: 100 Days of Code: The Complete Python Pro Bootcamp 
