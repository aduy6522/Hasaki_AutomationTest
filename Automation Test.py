import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set the PATH environment variable to include the directory containing msedgedriver.exe
os.environ['PATH'] += ';D:\\QC_Selenium\\edgedriver_win64\\'

# Initialize the Edge WebDriver without specifying the executable_path
driver = webdriver.Edge()

# Open the Hasaki website
driver.get('https://hasaki.vn/')

try:
    # Turn off the OneSignal notification element
    onesignal_dialog = driver.find_element(By.ID, 'onesignal-slidedown-dialog')
    driver.execute_script("arguments[0].style.display = 'none';", onesignal_dialog)
    
    # Wait for the page to load completely
    time.sleep(3)  # Adjust the sleep time as needed
    
    # Locate the "Đăng ký ngay" button using its class name
    register_button = driver.find_element(By.CLASS_NAME, 'popup-register')
    
    # Perform an action with the element, such as clicking it
    register_button.click()
finally:
    # Close the browser
    driver.quit()