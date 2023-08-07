from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

ACCOUNT_EMAIL = "khanbike222@gmail.com"
ACCOUNT_PASSWORD ="haripur999"

chrome_driver_path = ("C:\Windows\chromedriver.exe")

# Optional - Automatically keep your chromedriver up to date.from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Get the path to the Chrome driver executable
# chrome_driver_path = ChromeDriverManager().install()

# Optional - Keep the browser open if the script crashes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create a service object with the Chrome driver path
service = Service(chrome_driver_path)

# Create a Chrome driver instance with the service and options
driver = webdriver.Chrome(service=service, options=chrome_options)


driver.get("https://accounts.google.com/o/oauth2/v2/auth/identifier?client_id=1060018310736-l2r63l6edmjo06u90605n3ireop649b9.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fwww.fiverr.com%2Fauthentications%2Fgoogle%2Fcallback&response_type=code&scope=profile%20email&state=743e81440ee44b25b575cbb2bf4c7534&nonce=e9f2aac8abad4a34a9b10f441eee7efa&service=lso&o2v=2&flowName=GeneralOAuthFlow")
# input("tas")
# Click Reject Cookies Button
time.sleep(2)
# reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
# reject_button.click()

# Click Sign in Button
time.sleep(2)
sign_in_button = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
# sign_in_button.click()
# time.sleep(10)
sign_in_button.send_keys(ACCOUNT_EMAIL)

driver.find_element(By.XPATH,value='//*[@id="identifierNext"]/div/button/span').click()


# Sign in
time.sleep(5)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

# CAPTCHA - Solve Puzzle Manually
input("Press Enter when you have solved the Captcha")

# Get Listings
time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# Apply for Jobs
for listing in all_listings:
    button= listing.find_element(by=By.TAG_NAME,value='a')
    print(f"this is listing:   {button.text}")
    # print(f'"this is listing" {listing.find_elements(By.TAG_NAME,value="a")'}))
    print("Opening Listing")
    try:
        button.click()
    except:
        listing.click()
    time.sleep(5)
    apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
    apply_button.click()

        # Insert Phone Number
        # Find an <input> element where the id contains phoneNumber
    time.sleep(5)
    phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
    if phone.text == "":
        phone.send_keys(" ")


