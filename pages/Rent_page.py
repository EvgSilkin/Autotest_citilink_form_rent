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

    url = "https://www.citilink.ru/rent/"

    #Locators
    button_open_rent_form = "//button[@class='header__button-tab header__callback-tab popup']"
    input_rent_name = "//input[@name='rent[name]']"
    input_rent_phone = "//input[@name='rent[phone]']"
    input_rent_mail = "//input[@name='rent[email]']"
    input_rent_city = "//input[@name='rent[city]']"
    input_rent_description = "//input[@name='rent[description]']"
    button_send_application = "//button[@id='addSuggestion']"
    answer_heading = "//h2[@class='answer__heading']"

    #Getters
    def get_button_open_rent_form(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_open_rent_form)))
    def get_input_rent_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.input_rent_name)))
    def get_input_rent_phone(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.input_rent_phone)))
    def get_input_rent_mail(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.input_rent_mail)))
    def get_input_rent_city(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.input_rent_city)))
    def get_input_rent_description(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.input_rent_description)))
    def get_button_send_application(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_send_application)))
    def get_answer_heading(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.answer_heading)))
    def get_answer_heading_text(self):
        return self.get_answer_heading().text

    #Actions
    def click_button_open_rent_form(self):
        self.get_button_open_rent_form().click()

    #Methods
    def fill_input_rent_name(self, name):
        with allure.step("Input rent name"):
            Logger.add_start_step(method="Input rent name")
            self.get_input_rent_name().send_keys(name)
            Logger.add_end_step(url=self.get_current_url(), method="Input rent name")
    def fill_input_rent_phone(self, name):
        with allure.step("Input rent phone"):
            Logger.add_start_step(method="Input rent phone")
            self.get_input_rent_phone().send_keys(name)
            Logger.add_end_step(url=self.get_current_url(), method="Input rent phone")
    def fill_input_rent_mail(self, name):
        with allure.step("Input rent mail"):
            Logger.add_start_step(method="Input rent mail")
            self.get_input_rent_mail().send_keys(name)
            Logger.add_end_step(url=self.get_current_url(), method="Input rent mail")
    def fill_input_rent_city(self, name):
        with allure.step("Input rent city"):
            Logger.add_start_step(method="Input rent city")
            self.get_input_rent_city().send_keys(name)
            Logger.add_end_step(url=self.get_current_url(), method="Input rent city")
    def fill_input_rent_description(self, name):
        with allure.step("Input rent description"):
            Logger.add_start_step(method="Input rent description")
            self.get_input_rent_description().send_keys(name)
            Logger.add_end_step(url=self.get_current_url(), method="Input rent description")
    def send_application(self):
        with allure.step("Send application"):
            Logger.add_start_step(method="Send application")
            self.get_button_send_application().click()
            Logger.add_end_step(url=self.get_current_url(), method="Send application")
    def open_rent_form(self):
        with allure.step("Open rent form"):
            Logger.add_start_step(method="Open rent form")
            self.open_page(self.url)
            print("Current url: " + self.get_current_url())
            self.click_button_open_rent_form()
            Logger.add_end_step(url=self.get_current_url(), method="Open rent form")