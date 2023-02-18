from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *


"""Раздел «Конструктор» Проверь, что работают переходы"""
def test_chois_constructor_section_sauce_sucsses(login_user_from_main_page):
    driver = login_user_from_main_page

    #Проверяем переход к начинкам
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, filling)))
    driver.find_element(By.XPATH, filling).click()

    # выбираем нужный нам ингредиент "Сыр с астероидной плесенью"
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable((By.XPATH, filling)))
    driver.find_element(By.XPATH, fillings_cheese_with_asteroid_mold).click()

    assert driver.find_element(By.XPATH, asteroid_mold_check).text == 'Сыр с астероидной плесенью'

    driver.quit()