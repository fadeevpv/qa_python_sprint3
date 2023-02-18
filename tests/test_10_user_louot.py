from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *

"""Проверяем выход из аккаунта"""
def test_logout_from_user_profile_success(login_user_from_personal_page):
    driver = login_user_from_personal_page

    #переходим в личный кабинет
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, button6_personal_page_from_main_page)))
    driver.find_element(By.XPATH, button6_personal_page_from_main_page).click()

    # выполняет выход из аккаунта
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, button10_logout)))
    driver.find_element(By.XPATH, button10_logout).click()

    # проверяем что пользоветль вышел из аккаунта
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, button1_inter_user_page)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    driver.quit()
