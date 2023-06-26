from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

#initiate the chrome browser
browser = Chrome()
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

time.sleep(5)

#inputs asking emailId and password
EMAIL_ID = input("Enter email: ")
Password = input("Enter password: ")


#function to enter the email and password
def slow_typing(element, text):
   for character in text:
      element.send_keys(character)
      time.sleep(0.3)


#enter the email address in the form
form_tags = browser.find_elements(By.CLASS_NAME ,'form-field')
email = form_tags[0]
slow_typing(email, EMAIL_ID)

time.sleep(1)

#enter the password in the login form
password = form_tags[1]
slow_typing(password, Password)

time.sleep(0.5)

#click on the signIn button
sign_in_btn = browser.find_element(By.CLASS_NAME, 'button--branding')
sign_in_btn.click()

time.sleep(15)

#watch the first video
videos = browser.find_elements(By.CLASS_NAME, 'videothumbnail')
first_video = videos[0]
first_video.click()

time.sleep(10)
browser.close()