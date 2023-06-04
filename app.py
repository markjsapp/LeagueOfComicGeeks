from dotenv import dotenv_values
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

# Load environment variables from .env file
envs = dotenv_values()

# Configure the WebDriver with the path to the ChromeDriver executable
driver = webdriver.Chrome(executable_path=envs['CHROME'])  # Replace with the path to your ChromeDriver executable

# Load the webpage
url = 'https://leagueofcomicgeeks.com/'
driver.get(url)

try:
    # Use WebDriverWait along with ExpectedCondition to wait until the element is clickable
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//a[text()='Login'])[2]")))
    actual_element = driver.find_element(By.XPATH, "(//a[text()='Login'])[2]")
    actual_element.click()

    email_field_element = driver.find_element(By.XPATH, "//input[@type='text'][@name='username']")
    email_field_element.click()
    email_field_element.send_keys(envs['EMAIL'])

    password_field_element = driver.find_element(By.XPATH, "//input[@type='password'][@name='password']")
    password_field_element.click()
    password_field_element.send_keys(envs['PASSWORD'])

    submit_button_element = driver.find_element(By.XPATH, "//input[@id='submit']")
    submit_button_element.click()
except Exception as e:
    print('Error finding the element:')
    print(e)
finally:
    driver.quit()

# Extract the page source after the action
#page_source = driver.page_source

# Parse the page source with BeautifulSoup
#soup = BeautifulSoup(page_source, 'html.parser')

# Extract the desired data using BeautifulSoup methods
# Example: extracting text from an element
#data = soup.find('div', class_='your-class-name').text

# Close the browser
#driver.quit()

# Print the extracted data
#print(data)
