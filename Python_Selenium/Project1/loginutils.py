from selenium import webdriver

def test_check_login(login):
    assert login.find_element_by_xpath("/html/body/form/table/tbody/tr[1]/td[1]").text=="UserID"
    assert login.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[1]").text == "Password"
    assert len(login.find_elements_by_name('uid')) > 0
    assert len(login.find_elements_by_name('password')) > 0
    assert login.find_element_by_xpath('/html/body/form/table/tbody/tr[3]/td[2]/input[1]').get_attribute('value')=="LOGIN"
    assert login.find_element_by_xpath('/html/body/form/table/tbody/tr[3]/td[2]/input[2]').get_attribute('value')== "RESET"
