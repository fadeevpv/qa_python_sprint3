from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *


"""Раздел «Конструктор» Проверь, что работают переходы"""
def test_chois_constructor_section_roll_sucsses(login_user_from_main_page):
    driver = login_user_from_main_page

    # Проверяем переход к начинкам чтобы убедиться что мы можем переходить по разделам
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable((By.XPATH, sauces)))
    driver.find_element(By.XPATH, sauces).click()

    #переходим в раздел булки
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable((By.XPATH, rolls)))
    driver.find_element(By.XPATH, rolls).click()

    #выбираем нужную нам булку
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable((By.XPATH, filling)))
    driver.find_element(By.XPATH, rolls_crater_roll_n_200i).click()

    assert driver.find_element(By.XPATH, rolls_crater_check).text == 'Краторная булка N-200i'

    driver.quit()