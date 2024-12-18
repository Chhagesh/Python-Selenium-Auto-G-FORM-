from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 20)

try:
    # Open the Google Form
    form_url = "https://forms.gle/WT68aV5UnPajeoSc8"
    driver.get(form_url)
    time.sleep(2)  # Let the form load completely

    # Fill in the Full Name
    full_name = wait.until(EC.presence_of_element_located((By.XPATH, '(//input[@type="text"])[1]')))
    full_name.send_keys("Chhagesh Sahu")
    time.sleep(1)

    # Fill in the Contact Number
    contact_number = wait.until(EC.presence_of_element_located((By.XPATH, '(//input[@type="text"])[2]')))
    contact_number.send_keys("7879556952")
    time.sleep(1)

    # Fill in the Email ID
    email_id = wait.until(EC.presence_of_element_located((By.XPATH, '(//input[@type="text"])[3]')))
    email_id.send_keys("chhagesh30@gmail.com")
    time.sleep(1)

    # Fill in the Full Address
    full_address = wait.until(EC.presence_of_element_located((By.XPATH, '//textarea')))
    full_address.send_keys("Raipur, Chhattisgarh, India")
    time.sleep(1)

    # Fill in the Pin Code
    pin_code = wait.until(EC.presence_of_element_located((By.XPATH, '(//input[@type="text"])[4]')))
    pin_code.send_keys("492003")
    time.sleep(1)

    # Fill in the Date of Birth
    date_of_birth = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="date"]')))
    date_of_birth.send_keys("30/08/2005")
    time.sleep(1)

    # Select Gender (Radio Button)
    gender = wait.until(EC.presence_of_element_located((By.XPATH, '(//input[@type="text"])[5]')))
    gender.send_keys("Male")
    time.sleep(1)

    # Fill in the Verification Code
    verification_code = wait.until(EC.presence_of_element_located((By.XPATH, '(//input[@type="text"])[6]')))
    verification_code.send_keys("GNFPYC")
    time.sleep(1)

    # Submit the form
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Submit")]')))
    driver.execute_script("arguments[0].click();", submit_button)

    # Wait for confirmation
    time.sleep(2)
    driver.save_screenshot('confirmation_page.png')

finally:
    driver.quit()
