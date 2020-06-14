from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import importlib


class BasePage:
    def __init__(self, driver=None, url=None):
        self.driver = driver
        self.url = url

    def __exit__(self, exception_type, exception_value, traceback):
        self.driver.quit()


class JinjerExecService(object):
    def __init__(self, request):
        self.request = request
        self.driver = WebdriverWrapper()

    def create_webdriver_instance(self):
        try:
            importlib.import_module('chromedriver_binary')
            instance = webdriver.Chrome(options=get_options())
        except ModuleNotFoundError:
            print('Not found chromedriverbinary. so use config path')
            instance = webdriver.Chrome(
                executable_path="/usr/bin/chromedriver", options=get_options())
        # except AttributeError:
        #     print('メソッドが見つからない')
        return instance

    def checkin(self):
        self.driver


def get_options():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-features=VizDisplayCompositor')
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1280x800')
    # options.add_argument('--disable-application-cache')
    # options.add_argument('--disable-infobars')
    # options.add_argument('--hide-scrollbars')
    # options.add_argument('--enable-logging')
    # options.add_argument('--log-level=0')
    # options.add_argument('--single-process')
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--homedir=/tmp')
    # options.binary_location = '/usr/bin/google-chrome'
    return options


class WebdriverWrapper:
    def __init__(self):
        self._opt = get_options()
        self._driver = None
        # optの初期化コード

    def __enter__(self):
        try:
            importlib.import_module('chromedriver_binary')
            self._driver = webdriver.Chrome(options=self._opt)
        except ModuleNotFoundError:
            print('Not found chromedriverbinary. so use config path')
            self._driver = webdriver.Chrome(
                executable_path="/usr/bin/chromedriver", options=self._opt)

    def __exit__(self, exception_type, exception_value, traceback):
        self._driver.quit()
