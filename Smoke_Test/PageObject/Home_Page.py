from selenium import webdriver

class Home_Page:
    username_by_name='username'
    password_by_name='password'
    login_button_by_class_name='ui-button-text'
    def __init__(self,driver):
        self.driver=driver

    def send_username(self,username):
        self.driver.find_element_by_name(self.username_by_name).send_keys(username)

    def send_password(self,password):
        self.driver.find_element_by_name(self.password_by_name).send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_class_name(self.login_button_by_class_name).click()




