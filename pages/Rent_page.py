import allure

from base.Base import Base
from utilities.Logger import Logger

class Rent_page(Base):

    def __init__(self, driver):
        super().__init__(driver);
        self.driver = driver;

    url = "https://www.citilink.ru/rent/"

    #Locators
    button_open_rent_form = "//button[@class='header__button-tab header__callback-tab popup']"
    button_close_rent_form = "//button[contains(@class, 'js--RentPopup__popup__close')]"
    button_send_application = "//button[@id='addSuggestion']"
    button_less_40_meters = "//label[@for='radio_size1']"
    button_more_150_meters = "//label[@for='radio_size2']"
    input_rent_name = "//input[@name='rent[name]']"
    wrapper_input_rent_name = "//input[@name='rent[name]']/ancestor::div[contains(@class,'InputBox_has-label')]"
    input_rent_phone = "//input[@name='rent[phone]']"
    wrapper_input_rent_phone = "//input[@name='rent[phone]']/ancestor::div[contains(@class,'InputBox_has-label')]"
    input_rent_mail = "//input[@name='rent[email]']"
    wrapper_input_rent_mail = "//input[@name='rent[email]']/ancestor::div[contains(@class,'InputBox_has-label')]"
    input_rent_city = "//input[@name='rent[city]']"
    wrapper_input_rent_city = "//input[@name='rent[city]']/ancestor::div[contains(@class,'InputBox_has-label')]"
    input_rent_description = "//input[@name='rent[description]']"
    answer_heading = "//h2[@class='answer__heading']"
    form_heading = "//h2[@class='RentFeedback__title']"
    wrapper_button_less_40_meters = "//div[contains(@class, 'feedback-radio-less')]"
    wrapper_button_more_150_meters = "//div[contains(@class, 'feedback-radio-more')]"

    "//input[@name='rent[name]']/ancestor::div[contains(@class,'InputBox_has-label')]//div[@class='InputBox__error']"

    #Getters
    def get_button_open_rent_form(self):
        return self.get_element_to_be_clickable_by_xpath(self.button_open_rent_form)
    def get_button_close_rent_form(self):
        return self.get_element_to_be_clickable_by_xpath(self.button_close_rent_form)
# Rent Name Getters
    def get_input_rent_name(self):
        return self.get_element_to_be_clickable_by_xpath(self.input_rent_name)
    def get_wrapper_input_rent_name(self):
        return self.get_element_to_be_clickable_by_xpath(self.wrapper_input_rent_name)
# Rent Phone Getters
    def get_input_rent_phone(self):
        return self.get_element_to_be_clickable_by_xpath(self.input_rent_phone)
    def get_wrapper_input_rent_phone(self):
        return self.get_element_to_be_clickable_by_xpath(self.wrapper_input_rent_phone)
# Rent Mail Getters
    def get_input_rent_mail(self):
        return self.get_element_to_be_clickable_by_xpath(self.input_rent_mail)
    def get_wrapper_input_rent_mail(self):
        return self.get_element_to_be_clickable_by_xpath(self.wrapper_input_rent_mail)
# Rent City Getters
    def get_input_rent_city(self):
        return self.get_element_to_be_clickable_by_xpath(self.input_rent_city)
    def get_wrapper_input_rent_city(self):
        return self.get_element_to_be_clickable_by_xpath(self.wrapper_input_rent_city)
# Rent Descriptions Getters
    def get_input_rent_description(self):
        return self.get_element_to_be_clickable_by_xpath(self.input_rent_description)
    def get_button_send_application(self):
        return self.get_element_to_be_clickable_by_xpath(self.button_send_application)
# Other Input Getters
    def get_errors_input_element(self, input_name):
        locator_name = f"//input[@name='rent[{input_name}]']/ancestor::div[contains(@class,'InputBox_has-label')]//div[@class='InputBox__error']"
        return self.get_element_to_be_clickable_by_xpath(locator_name)
    def get_wrapper_input_element(self, input_name):
        locator_name = f"//input[@name='rent[{input_name}]']/ancestor::div[contains(@class,'InputBox_has-label')]"
        return self.get_element_to_be_clickable_by_xpath(locator_name)
    def get_input_by_inner_name(self, input_name):
        locator_name = f"//input[@name='rent[{input_name}]']"
        return self.get_element_to_be_clickable_by_xpath(locator_name)
# Marker Getters
    def get_answer_heading(self):
        return self.get_element_to_be_clickable_by_xpath(self.answer_heading)
    def get_form_heading(self):
        return self.get_element_to_be_clickable_by_xpath(self.form_heading)
    def get_answer_heading_text(self):
        return self.get_answer_heading().text
    def get_form_heading_text(self):
        return self.get_form_heading().text
# Area Getters
    def get_button_less_40_meters(self):
        return self.get_element_to_be_clickable_by_xpath(self.button_less_40_meters)
    def get_wrapper_button_less_40_meters(self):
        return self.get_element_to_be_clickable_by_xpath(self.wrapper_button_less_40_meters)
    def get_button_more_150_meters(self):
        return self.get_element_to_be_clickable_by_xpath(self.button_more_150_meters)
    def get_wrapper_button_more_150_meters(self):
        return self.get_element_to_be_clickable_by_xpath(self.wrapper_button_more_150_meters)

    #Actions
    def click_button_open_rent_form(self):
        self.get_button_open_rent_form().click()
    def click_button_send_application(self):
        with allure.step("Input rent phone"):
            Logger.add_start_step(method="Click button send application")
            self.get_button_send_application().click()
            Logger.add_end_step(url=self.get_current_url(), method="Click button send application")
    def click_button_close_rent_form(self):
        self.get_button_close_rent_form().click()
    def click_get_button_less_40_meters(self):
        self.get_button_less_40_meters().click()
    def click_get_button_more_150_meters(self):
        self.get_button_more_150_meters().click()
    def assert_input_value(self, input_name, value):
        input_item = self.get_input_by_inner_name(input_name)
        value_input_item = input_item.get_attribute("value")
        if input_name == "phone":
            value_input_item = self.clear_phone_value(value_input_item)
        assert value == value_input_item

    #Methods

    def open_page(self):
        with allure.step(f"Open page on {self.url}"):
            Logger.add_start_step(method=f"Open page on {self.url}")
            self.driver.get(self.url)
            self.driver.maximize_window()
            Logger.add_end_step(url=self.get_current_url(), method=f"Open page on {self.url}")
    def fill_input_rent_name(self, name):
        with allure.step("Input rent name"):
            Logger.add_start_step(method="Input rent name")
            self.get_input_rent_name().send_keys(name)
            self.assert_element_text(name, self.get_input_rent_name().get_attribute('value'))
            Logger.add_end_step(url=self.get_current_url(), method="Input rent name")
    def fill_input_rent_phone(self, phone):
        with allure.step("Input rent phone"):
            Logger.add_start_step(method="Input rent phone")
            self.get_input_rent_phone().send_keys(phone)
            clear_phone_from_input = self.clear_phone_value(self.get_input_rent_phone().get_attribute('value'))
            self.assert_element_text(phone, clear_phone_from_input)
            Logger.add_end_step(url=self.get_current_url(), method="Input rent phone")
    def fill_input_rent_mail(self, mail):
        with allure.step("Input rent mail"):
            Logger.add_start_step(method="Input rent mail")
            self.get_input_rent_mail().send_keys(mail)
            self.assert_element_text(mail, self.get_input_rent_mail().get_attribute('value'))
            Logger.add_end_step(url=self.get_current_url(), method="Input rent mail")
    def fill_input_rent_city(self, city):
        with allure.step("Input rent city"):
            Logger.add_start_step(method="Input rent city")
            self.get_input_rent_city().send_keys(city)
            self.assert_element_text(city, self.get_input_rent_city().get_attribute('value'))
            Logger.add_end_step(url=self.get_current_url(), method="Input rent city")
    def fill_input_rent_description(self, description):
        with allure.step("Input rent description"):
            Logger.add_start_step(method="Input rent description")
            self.get_input_rent_description().send_keys(description)
            self.assert_element_text(description, self.get_input_rent_description().get_attribute('value'))
            Logger.add_end_step(url=self.get_current_url(), method="Input rent description")
    def send_application(self, text_marker):
        with allure.step("Send application"):
            Logger.add_start_step(method="Send application")
            self.click_button_send_application()
            self.assert_element_text(text_marker, self.get_answer_heading_text())
            Logger.add_end_step(url=self.get_current_url(), method="Send application")
    def open_rent_form(self, form_marker):
        with allure.step("Open rent form"):
            Logger.add_start_step(method="Open rent form")
            self.click_button_open_rent_form()
            self.assert_element_text(form_marker, self.get_form_heading_text())
            Logger.add_end_step(url=self.get_current_url(), method="Open rent form")
    def close_rent_form(self):
        with allure.step("Close rent form"):
            Logger.add_start_step(method="Close rent form")
            self.click_button_close_rent_form()
            Logger.add_end_step(url=self.get_current_url(), method="Close rent form")
    def change_form_to_area_less_40_metres(self, value_for_assert):
        with allure.step("Change form to area less 40 metres"):
            Logger.add_start_step(method="Change form to area less 40 metres")
            self.click_get_button_less_40_meters()
            element_class_value = self.get_wrapper_button_less_40_meters().get_attribute('class')
            self.assert_element_text(value_for_assert, element_class_value)
            Logger.add_end_step(url=self.get_current_url(), method="Change form to area less 40 metres")
    def change_form_to_area_more_150_metres(self, value_for_assert):
        with allure.step("Change form to area more 150 metres"):
            Logger.add_start_step(method="Change form to area more 150 metres")
            self.click_get_button_more_150_meters()
            element_class_value = self.get_wrapper_button_more_150_meters().get_attribute('class')
            self.assert_element_text(value_for_assert, element_class_value)
            Logger.add_end_step(url=self.get_current_url(), method="Change form to area more 150 metres")
    def get_and_assert_input_value(self, input_name, value):
        with allure.step(f"Get and assert {input_name}-input value"):
            Logger.add_start_step(method=f"Get and assert {input_name}-input value")
            self.assert_input_value(input_name, value)
            Logger.add_end_step(url=self.get_current_url(), method=f"Get and assert {input_name}-input value")
    def assert_errors_input_message(self, input_name, value):
        with allure.step(f"Assert errors input rent {input_name} message"):
            Logger.add_start_step(method=f"Assert errors input rent {input_name} message")
            text_errors_input_element = self.get_errors_input_element(input_name).text
            self.assert_element_text(text_errors_input_element, value)
            Logger.add_end_step(url=self.get_current_url(), method=f"Assert errors input rent {input_name} message")
    def assert_class_contains_str(self, input_name, value):
        with allure.step(f"Assert class input rent {input_name} contains '{value}'"):
            Logger.add_start_step(method=f"Assert class input rent {input_name} contains '{value}'")
            wrapper_input_element = self.get_wrapper_input_element(input_name)
            class_wrapper_input_element = wrapper_input_element.get_attribute("class")
            self.assert_class_contains(class_wrapper_input_element, value)
            Logger.add_end_step(url=self.get_current_url(), method=f"Assert class input rent {input_name} contains '{value}'")

