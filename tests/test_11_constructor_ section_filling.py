from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *


"""Раздел «Конструктор» Проверь, что работают переходы"""
def test_chois_constructor_section_filling_sucsses(login_user_from_main_page):
    driver = login_user_from_main_page

    #Проверяем переход к начинкам
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable((By.XPATH, sauces)))
    driver.find_element(By.XPATH, sauces).click()

    # выбираем нужный нам ингредиент "Сыр с астероидной плесенью"
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable((By.XPATH, sauces_traditional_galactic_sauce)))
    driver.find_element(By.XPATH, sauces_traditional_galactic_sauce).click()

    assert driver.find_element(By.XPATH, galactic_sauce_check).text == 'Соус традиционный галактический'

    driver.quit()