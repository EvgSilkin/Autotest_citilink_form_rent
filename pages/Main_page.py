import allure

from base.Base import Base
from utilities.Logger import Logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver);
        self.driver = driver;

    url = "https://www.citilink.ru/"

    #Locators
    link_to_forum_page = "//a[@href='https://forum.citilink.ru']"
    link_to_rent_page = "//a[@href='/rent/']"
    button_accept_cookie = "//button[@class='e4uhfkv0 css-1jfe691 e4mggex0']"

    #Getters
    def get_button_accept_cookie(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_accept_cookie)))
    def get_link_to_rent_page(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.link_to_rent_page)))

    #Actions
    def move_to_element(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_link_to_rent_page()).perform()
    def click_button_accept_cookie(self):
        self.get_button_accept_cookie().click()

    def click_link_to_rent_page(self):
        self.get_link_to_rent_page().click()

    #Methods
    def follow_to_rent_page(self):
        with allure.step("Follow to rent page"):
            Logger.add_start_step(method="Follow to rent page")
            self.open_page(self.url)
            print("Current url: " + self.get_current_url())
            self.click_button_accept_cookie()
            self.move_to_element()
            self.click_link_to_rent_page()
            Logger.add_end_step(url=self.get_current_url(), method="Follow to rent page")