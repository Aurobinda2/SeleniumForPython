#from selenium import webdriver

class LoginTest:
    user_id='txtUsername'
    password='txtPassword'
    login_button='btnLogin'

    def __init__(self,driver):
        self.driver=driver

    def set_UserName(self,username):
        self.driver.find_element_by_id(self.user_id).send_keys(username)

    def set_Password(self,password):
        self.driver.find_element_by_id(self.user_id).send_keys(password)

    def login_action(self):
        self.driver.find_element_by_id(self.login_button).click()



