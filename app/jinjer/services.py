'''Jinjer操作サービス'''
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class LoginPageLocators(object):
    '''
    [Location]
    Login Page
    '''
    COMPANY_CODE_TEXT = (By.ID, 'company_code')
    ID_TEXT = (By.NAME, 'email')
    PASSWORD_TEXT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.ID, 'jbtn-login-staff')


class MainPageLocators(object):
    '''
    [Location]
    Main Page
    '''
    CHECK_IN_BUTTON = (By.XPATH,
                       '//*[@id="container"]//button[@data-type="check_in"]')
    CHECK_OUT_BUTTON = (By.XPATH,
                        '//*[@id="container"]//button[@data-type="check_out"]')


def login(driver):
    '''
    [Control]
    ログイン
    '''
    driver.get("https://kintai.jinjer.biz/staffs/top")
    driver.find_element(*LoginPageLocators.COMPANY_CODE_TEXT).send_keys(
        os.getenv("DJANGO_JINJER_COMPANY_CODE"))
    driver.find_element(*LoginPageLocators.ID_TEXT).send_keys(
        os.getenv("DJANGO_JINJER_EMAIL"))
    driver.find_element(*LoginPageLocators.PASSWORD_TEXT).send_keys(
        os.getenv("DJANGO_JINJER_PASSWORD"))
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    print('[Success]:Login.')


def check_in(driver):
    '''
    [Control]
    出勤
    '''
    element = WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(
            MainPageLocators.CHECK_IN_BUTTON))
    element.click()
    print('[Success]:Check In.')


def check_out(driver):
    '''
    [Control]
    退勤
    '''
    element = WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(
            MainPageLocators.CHECK_OUT_BUTTON))
    element.click()
    print('[Success]:Check Out.')
