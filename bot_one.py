from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

#initiate the chrome browser and get the url
options = webdriver.ChromeOptions()
browser = Chrome(options=options)
browser.get('https://www.fruitlab.com')
browser.maximize_window()

time.sleep(1)

#the agree modal form
modal_btn = browser.find_element(By.XPATH, '//html/body/div/div/div/div/div[2]/div/button[2]')
modal_btn.click()

time.sleep(2)

# click on the SignIn/register button
register_btn_div = browser.find_element(By.CLASS_NAME, 'header--login')
register_btn = register_btn_div.find_element(By.TAG_NAME, 'button')
register_btn.click()

time.sleep(2)

#click on create account button
login_id = browser.find_element(By.ID, 'login')
div_tags = login_id.find_elements(By.CLASS_NAME, 'main-area__content--login-form-normal-text')
btn = div_tags[2].find_element(By.TAG_NAME, 'button')
btn.click()

time.sleep(5)

#function to enter the email and password
def slow_typing(element, text):
   for character in text:
      element.send_keys(character)
      time.sleep(0.3)

#inputs asking emailId and password
EMAIL_ID = input('Enter your email: ')
Password = input('Enter password: ')

#enter the email address
form_tags = browser.find_elements(By.CLASS_NAME ,'form-field')
email = form_tags[0]
slow_typing(email, EMAIL_ID)

time.sleep(3)

#enter the password
password = form_tags[1]
slow_typing(password, Password)

time.sleep(2)

#confirm the password again
confirm_password = form_tags[2]
slow_typing(confirm_password, Password)

time.sleep(3)

#checkbox to agree terms and conditions
checkbox = browser.find_element(By.ID, 'signup_terms')
checkbox.click()

#click the sign up button
signup_btn = browser.find_element(By.ID, 'btn_registerform')
signup_btn.click()

time.sleep(5)
browser.close()
