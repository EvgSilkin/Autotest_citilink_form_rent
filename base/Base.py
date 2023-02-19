import datetime

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wait

from utilities.Logger import Logger


class Base():

    def __init__(self, driver):
        self.driver = driver;

    def open_page(self, url):
        with allure.step(f"Open page on {url}"):
            Logger.add_start_step(method=f"Open page on {url}")
            self.driver.get(url)
            self.driver.maximize_window()
            Logger.add_end_step(url=self.get_current_url(), method=f"Open page on {url}")

    def get_current_url(self):
        return self.driver.current_url
    def get_element_to_be_clickable_by_xpath(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, locator)))
    def assert_element_text(self, text, result):
        assert text == result

    def assert_url(self, result):
        current_url = self.get_current_url()
        assert current_url == result

    def screen_page(self, path):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        print("before screen")
        self.driver.save_screenshot(f"{path}{name_screenshot}")
        print("screen path " + f"{path}{name_screenshot}")
        print("after screen")

    def clear_phone_value(self, phone):
        remove_list = ["(", ")", "-"]
        if len(phone) > 3:
            ranged_phone = phone[3:]
            ranged_phone = ranged_phone.replace("(", "")
            ranged_phone = ranged_phone.replace(")", "")
            ranged_phone = ranged_phone.replace("-", "")
            ranged_phone = ranged_phone.replace(" ", "")
        return ranged_phone

