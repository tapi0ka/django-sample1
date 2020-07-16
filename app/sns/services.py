'''Jinjer操作サービス'''
import os

import time
from urllib.parse import urlparse


from django.utils import timezone


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

from sns.models import Reports
from collections import defaultdict



class LoginPageLocators(object):
    '''
    [Location]
    Login Page
    '''
    USERNAME_TEXT = (By.ID, 'username')
    PASSWORD_TEXT = (By.ID, 'password')
    LOGIN_BUTTON = (By.XPATH, '//*[@id=\"button_login\"]')

class ReportSearchLocators(object):
    '''
    月報検索画面
    '''
    REPORT_DETAIL_URLS = (By.XPATH, '//table[@border="1" and @cellspacing="0"]/tbody/tr/td[1]//a')
    YM_DROPDOWN = (By.NAME, 'report_ym')
    SUBMIT_BUTTON = (By.XPATH, '//td/input')

class ReportDetailLocators(object):
    '''
    月報詳細画面
    '''
    REPORT_DETAIL_ITEMS = (By.XPATH, '//form[1]/table/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div')

def login(driver):
    '''
    [Control]
    ログイン
    '''
    print('[Start]:Login.')
    basic_info = os.getenv("DJANGO_SNS_BASIC_USER") + ':' + os.getenv('DJANGO_SNS_BASIC_PASS') + '@'
    driver.get("https://" + basic_info + "sv27.wadax.ne.jp/~stylagy-co-jp/sns/")

    driver.find_element(*LoginPageLocators.USERNAME_TEXT).send_keys(os.getenv('DJANGO_SNS_EMAIL'))
    driver.find_element(*LoginPageLocators.PASSWORD_TEXT).send_keys(os.getenv('DJANGO_SNS_PSSSWORD'))
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    print('[Complete]:Login.')

def select_dropdown(driver, ym):
    '''
    うまく動かないので使用しない
    '''
    element = driver.find_element(*ReportSearchLocators.YM_DROPDOWN)
    ym_dropdown = Select(element)
    ym_dropdown.select_by_value(ym)
    print(driver.page_source)

    # ここでエラー発生する。。。10秒待つようにしているが要素が見つからないっぽい
    submit_element = WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(
        ReportSearchLocators.SUBMIT_BUTTON)
    )

    submit_element.click()



def get_report_urls(driver, ym):
    '''
    月報のURLを取得する
    '''
    driver.get("https://sv27.wadax.ne.jp/~stylagy-co-jp/sns/?m=pc&a=page_h_report_m_search")
    elements = driver.find_elements(*ReportSearchLocators.REPORT_DETAIL_URLS)

    # if ym is None:
    #     pass
    # else:
        # ドロップダウンから必要な月報の年月を選択するはず。。。
        # select_dropdown(driver, ym)

    urllist = []
    for i in range(len(elements)):
        if not elements[i].text:
            continue # 月報を書いてない人のURLは取得しない
        urllist.append(elements[i].get_attribute('href'))

    print(urllist)

    return urllist

def open_report_detail(driver, url):
    '''
    月報のURLを取得する
    '''
    driver.get(url)

    o = urlparse(url)
    print(o)

    # print(driver.page_source) # 開いているURLのHTMLを確認する


    # FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image/screen.png")
    # print(FILENAME)
    # driver.save_screenshot(FILENAME)

    elements = driver.find_elements(*ReportDetailLocators.REPORT_DETAIL_ITEMS)
    elements_iter = iter(elements)
    d = defaultdict(lambda:'')
    while True:
        try:
            item_name = elements_iter.__next__().text
            if check_item(item_name):
                d[item_name] = elements_iter.__next__().text
        except StopIteration:
            break

    obj = Reports(
        submitter=d['提出者'],
        submission_year_month=d['提出年月'],
        work_place=d['作業場所'],
        work_content=d['作業内容'],
        environment=d['環境\n（使用しているOS/言語/アプリケーションなど）'],
        problem=d['問題点/懸念事項'],
        self_assessment=d['自己評価'],
        acquisition_skill=d['習得したスキル\n又は\n習得中のスキル'],
        work_schedule=d['今後の作業予定'],
        goal=d['来月の目標\n又は\n習得したいスキル'],
        other=d['そ の 他'],
        created_at=timezone.now(),
        updated_at=timezone.now(),
        )

    obj.save()

    return

def check_item(str):
    '''
    月報項目かをチェックする
    '''
    if str in {'提出者','提出年月','作業場所','作業内容','環境\n（使用しているOS/言語/アプリケーションなど）','問題点/懸念事項','自己評価',"習得したスキル\n又は\n習得中のスキル",'今後の作業予定','来月の目標\n又は\n習得したいスキル','そ の 他'}:
        return True
    return False
