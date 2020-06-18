import os
import importlib
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from jinjer.models import ExecList


def login(driver):
    driver.get("https://kintai.jinjer.biz/staffs/top")
    driver.find_element(*LoginPageLocators.COMPANY_CODE_TEXT).send_keys(
        os.getenv("DJANGO_JINJER_COMPANY_CODE"))
    driver.find_element(*LoginPageLocators.ID_TEXT).send_keys(
        os.getenv("DJANGO_JINJER_EMAIL"))
    driver.find_element(*LoginPageLocators.PASSWORD_TEXT).send_keys(
        os.getenv("DJANGO_JINJER_PASSWORD"))
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    print('[Success] Login.')


class LoginPageLocators(object):
    '''
    [Location] Login Page
    '''
    COMPANY_CODE_TEXT = (By.ID, 'company_code')
    ID_TEXT = (By.NAME, 'email')
    PASSWORD_TEXT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.ID, 'jbtn-login-staff')


def checkIn(driver):
    # syukkin_button = (By.XPATH,
    #                   '//*[@id="container"]//button[@data-type="check_in"]')
    print("checkin")
    time.sleep(5)
    syukkin_button = '//*[@id="container"]//button[@data-type="check_in"]'
    print(syukkin_button)
    driver.find_element(By.XPATH, syukkin_button).click()

    print('[Success] Clocking In.')


def checkOut(driver):
    taikin_button = (By.XPATH,
                     '//*[@id="container"]//button[@data-type="check_out"]')
    driver.find_element(
        '//*[@id="container"]//button[@data-type="check_out"]').click()
    print('[Success] Clocking Out.')
