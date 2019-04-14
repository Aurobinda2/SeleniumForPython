from selenium import webdriver
class Initaite:
    username_parameter='username'
    password_parameter='password'
    login_button_id='tdb1'
    def __init__(self,driver):
        self.driver=driver

    def set_url(self,url):
        self.driver.get(url)
        self.driver.maximize_window()
        return self.driver.title

    def set_username(self,username):
        self.driver.find_element_by_name(self.username_parameter).send_keys(username)


    def set_password(self,password):
        self.driver.find_element_by_name(self.username_parameter).send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_id(self.login_button_id)

