# This project utilizes Selenium and BeautifulSoup to track price and mail when price is lower than threshold.
import os
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import smtplib
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# URL of the product
url = "product_url_to_track"
# Email credentials from environment variables
email = "user_gmail_address"
pswrd = "user_app_password"

#threshold price
threshold_price = "threshold_value_as_integer"

# Set up Chrome driver in headless mode (Headless mode allows to not open the GUI of the website, it will open in background)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# Wait until price is loaded- waits till price element is loaded
wait = WebDriverWait(driver, 10)
price_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole")))

# Get the page source elements and parse it with BeautifulSoup
page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")
driver.quit()

# Extract price and item name
try:
    price_tag_whole = soup.find('span', class_="a-price-whole")
    price_tag_fraction = soup.find('span', class_="a-price-fraction")
    numeric_price = float(price_tag_whole.text.replace(',', '') + price_tag_fraction.text)

    item_tag = soup.find('span', id="productTitle")
    item_name = item_tag.text.strip()

except AttributeError:
    print("Error: Could not retrieve price or product name. POSSIBLE ISSUE MAY BE CHANGE IN STRUCTURE OF AMAZON WEBPAGE.")
    numeric_price = None

# Check if the price has dropped below the threshold

if numeric_price and numeric_price < threshold_price:
    price_diff = threshold_price - numeric_price
    
    #create a template for the mail.
    email_message = f'''
Hi,
Good news! The price of the item you're tracking has dropped below your desired threshold.

Item: {item_name}

Threshold Price: Rs.{threshold_price}

New Price: Rs.{numeric_price}

You Save: Rs.{price_diff}

Buy now: {url}

Hurry up! Prices may change quickly, so don't miss out.
Happy shopping,
Your Amazon Price Tracker (APT)
'''

#Mailing Setup using smtplib module
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=email, password=pswrd)
            connection.sendmail(from_addr=email, to_addrs=email, msg=f"Subject: APT || Price Drop Alert!! \n\n{email_message}")
        print("Email sent successfully.")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")
