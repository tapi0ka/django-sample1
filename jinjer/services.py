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
    driver.find_element_by_id('company_code').send_keys(
        os.getenv("DJANGO_JINJER_COMPANY_CODE"))
    driver.find_element_by_name('email').send_keys(
        os.getenv("DJANGO_JINJER_EMAIL"))
    driver.find_element_by_name('password').send_keys(
        os.getenv("DJANGO_JINJER_PASSWORD"))
    driver.find_element_by_id('jbtn-login-staff').click()
    print('[Success] Login.')


def clockingIn(driver):
    syukkin_button = (By.XPATH, '//*[@id="container"]//button[@data-type="check_in"]')
    driver.find_element_by_xpath('//*[@id="container"]//button[@data-type="check_in"]').click()
    print('[Success] Clocking In.')


def clockingOut(driver):
    taikin_button = (By.XPATH,
                     '//*[@id="container"]//button[@data-type="check_out"]')
    driver.find_element(*taikin_button).click()
    print('[Success] Clocking Out.')
