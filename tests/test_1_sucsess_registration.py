from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *



"""Проверяем успешную регистрацию ногого пользователя пользователя"""

def test_new_user_registration_succes(new_user_registration):
    driver = new_user_registration

    #проверяем чторегистрация прошла и прошел редирект на форму вовда логина и пароля
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, button1_inter_user_page)))

    assert driver.find_element(By.XPATH, header_inter_page).text == 'Вход'
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    driver.quit()



