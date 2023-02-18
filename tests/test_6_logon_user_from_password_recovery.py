from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *

"""Проверяем вход через кнопку в форме восстановления пароля"""
def test_login_user_from_recovery_password_page(login_user_from_recovery_password_page):
    driver = login_user_from_recovery_password_page

    # проверям что после авторизации доступна кнопка оформить заказ
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, button3_take_order_main_page)))

    assert driver.find_element(By.XPATH, button3_take_order_main_page).text == 'Оформить заказ'

    driver.quit()