from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *

"""Проверяем переход от личного кабинеа в конструктор"""
def test_from_user_profile_to_constructor(login_user_from_personal_page):
    driver = login_user_from_personal_page

    #переходим в личный кабинет
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, button6_personal_page_from_main_page)))
    driver.find_element(By.XPATH, button6_personal_page_from_main_page).click()

    # переходим в конструктор бургеров
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, button9_inter_to_constructor)))
    driver.find_element(By.XPATH, button9_inter_to_constructor).click()

    # проверяем что мы перешли в окнструктор
    assert driver.find_element(By.XPATH, construct_burgers).text == 'Соберите бургер'

    driver.quit()