from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *

"""Проверяем вход через кнопку «Личный кабинет»"""

def test_login_user_from_personal_page_success(login_user_from_personal_page):
    driver = login_user_from_personal_page

    # проверям что после авторизации доступна кнопка оформить заказ
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, button3_take_order_main_page)))

    assert driver.find_element(By.XPATH, button3_take_order_main_page).text == 'Оформить заказ'

    driver.quit()