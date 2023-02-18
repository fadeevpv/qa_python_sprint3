import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from generator_credentionals import *
from locators import *


@pytest.fixture()  # авторизация по кнопке «Войти в аккаунт» на главной
def login_user_from_main_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(main_page)
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, button5_inter_account_main_page)))
    driver.find_element(By.XPATH, button5_inter_account_main_page).click()
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, button1_inter_user_page)))
    driver.find_element(By.XPATH, input_email_login_page).send_keys(user_mail)
    driver.find_element(By.XPATH, input_password_login_page).send_keys(user_password)
    driver.find_element(By.XPATH, button1_inter_user_page).click()
    return driver


@pytest.fixture()  # авторизация  через кнопку «Личный кабинет»
def login_user_from_personal_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(main_page)
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, button6_personal_page_from_main_page)))
    driver.find_element(By.XPATH, button6_personal_page_from_main_page).click()
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, button1_inter_user_page)))
    driver.find_element(By.XPATH, input_email_login_page).send_keys(user_mail)
    driver.find_element(By.XPATH, input_password_login_page).send_keys(user_password)
    driver.find_element(By.XPATH, button1_inter_user_page).click()
    return driver


@pytest.fixture()  # авторизация через кнопку в форме регистрации
def login_user_from_registration_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(registration_page)
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, button7_inter_from_registration_page)))
    driver.find_element(By.XPATH, button7_inter_from_registration_page).click()
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, button1_inter_user_page)))
    driver.find_element(By.XPATH, input_email_login_page).send_keys(user_mail)
    driver.find_element(By.XPATH, input_password_login_page).send_keys(user_password)
    driver.find_element(By.XPATH, button1_inter_user_page).click()
    return driver


@pytest.fixture()  # авторизация через кнопку в форме восстановления пароля
def login_user_from_recovery_password_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(recovery_password_page)
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, button8_inter_from_recovery_password_page)))
    driver.find_element(By.XPATH, button8_inter_from_recovery_password_page).click()
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, button1_inter_user_page)))
    driver.find_element(By.XPATH, input_email_login_page).send_keys(user_mail)
    driver.find_element(By.XPATH, input_password_login_page).send_keys(user_password)
    driver.find_element(By.XPATH, button1_inter_user_page).click()
    return driver


@pytest.fixture()
def new_user_registration():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(registration_page)
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable((By.XPATH, button2_reg_user_registartion_page)))
    driver.find_element(By.XPATH, input_name_user_reg_page).send_keys(user_lastname_generator())
    driver.find_element(By.XPATH, input_email_user_reg_page).send_keys(user_login_generator())
    driver.find_element(By.XPATH, input_user_password_reg_page).send_keys(user_password_generator())
    driver.find_element(By.XPATH, button2_reg_user_registartion_page).click()
    return driver


@pytest.fixture()
def new_user_registration_with_incorrect_password():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(registration_page)
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable((By.XPATH, button2_reg_user_registartion_page)))
    driver.find_element(By.XPATH, input_name_user_reg_page).send_keys(user_lastname_generator())
    driver.find_element(By.XPATH, input_email_user_reg_page).send_keys(user_login_generator())
    driver.find_element(By.XPATH, input_user_password_reg_page).send_keys('123')
    driver.find_element(By.XPATH, button2_reg_user_registartion_page).click()
    return driver

