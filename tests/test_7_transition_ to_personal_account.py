from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *

"""Проверь переход по клику на «Личный кабинет»."""

def test_open_user_profile_success(login_user_from_personal_page):
    driver = login_user_from_personal_page

    #переходим в личный кабинет
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, button6_personal_page_from_main_page)))
    driver.find_element(By.XPATH, button6_personal_page_from_main_page).click()

    # проверяем что пльзователь находиться на своей страничке пользователя
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, information_about_page)))
    assert driver.find_element(By.XPATH, information_about_page).text == 'В этом разделе вы можете изменить свои персональные данные'
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    driver.quit()