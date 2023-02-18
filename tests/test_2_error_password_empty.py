from selenium.webdriver.common.by import By
from locators import *

"""Проверяем ошибку при регистрации когда пользователь ввел не корректный пароль"""

def test_new_registration_user_fail_invalid_password(new_user_registration_with_incorrect_password):
    driver = new_user_registration_with_incorrect_password

    #проверяем ошибку некоректного ввода пароля
    assert driver.find_element(By.XPATH,
                               error_message_invalid_password_registartion_page).text == 'Некорректный пароль'

    driver.quit()