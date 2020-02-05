import pytest
from selenium import webdriver

@pytest.fixture()
def login():
    driver = webdriver.Firefox(executable_path='geckodriver.exe')
    driver.get('http://www.demo.guru99.com/V4')
    return driver