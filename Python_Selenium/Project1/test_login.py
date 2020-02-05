test_args="user_id,password,expected_result"
test_data='[(mngr244295,pesUdAp,"""Welcome To Manager's Page of Guru99 Bank""")

def test_check_login():
    driver.switchTo().alert().getText();