import allure

from base.Base import Base
from utilities.Logger import Logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Rent_page(Base):

    def __init__(self, driver):
        super().__init__(driver);
        self.driver = driver;

    #Locators
    button_submit_application = "//button[@class='header__button-tab header__callback-tab popup']"

    #Getters
    def get_button_submit_application(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_submit_application)))

    #Actions
    def click_button_submit_application(self):
        self.get_button_submit_application().click()

    #Methods
    def send_application(self):
        with allure.step("Send application"):
            Logger.add_start_step(method="Send application")
            print("Current url: " + self.get_current_url())
            self.click_button_submit_application()
            Logger.add_end_step(url=self.get_current_url(), method="Send application")