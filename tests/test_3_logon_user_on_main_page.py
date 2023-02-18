from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *

"""Тест проверить - вход по кнопке «Войти в аккаунт» на главной"""
def test_login_user_success(login_user_from_main_page):
    driver = login_user_from_main_page

    # проверям что после авторизации доступна кнопка оформить заказ
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, button3_take_order_main_page)))

    assert driver.find_element(By.XPATH, button3_take_order_main_page).text == 'Оформить заказ'


    driver.quit()