import time
import allure

from selenium import webdriver
from selenium.common import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
# from pages.Main_page import Main_page
from pages.Rent_page import Rent_page

@allure.description("test_buy_product")
def test_action1(set_up):

    driver = webdriver.Chrome(ChromeDriverManager().install())
    # path_to_screenshot = "..\\screen\\"
    text_marker = "Спасибо за заявку на сотрудничество"
    rent_page = Rent_page(driver)
    rent_page.open_rent_form()
    rent_page.fill_input_rent_name("Иванов Иван Иванович")
    rent_page.fill_input_rent_phone("9123456789")
    rent_page.fill_input_rent_mail("test@test.ru")
    rent_page.fill_input_rent_city("Казань Татарстан")
    rent_page.fill_input_rent_description("Цокольный этаж")
    time.sleep(7)
    rent_page.send_application()
    try:
        rent_page.assert_element_text(text_marker, rent_page.get_answer_heading_text())
    except TimeoutException:
        raise  TimeoutException("Text marker did`t find")
    finally:
        driver.close()

def test_action2(set_up):

    driver = webdriver.Chrome(ChromeDriverManager().install())
    # path_to_screenshot = "..\\screen\\"
    text_marker = "Спасибо за заявку на сотрудничество"
    rent_page = Rent_page(driver)
    rent_page.open_rent_form()
    rent_page.fill_input_rent_name("Иванов Иван Иванович")
    rent_page.fill_input_rent_phone("9123456789")
    rent_page.fill_input_rent_mail("test@test.ru")
    rent_page.fill_input_rent_city("Казань Татарстан")
    rent_page.fill_input_rent_description("Цокольный этаж")
    time.sleep(7)
    rent_page.send_application()
    rent_page.assert_element_text(text_marker, rent_page.get_answer_heading_text())
    driver.close()