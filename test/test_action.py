import time
import allure

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.Main_page import Main_page
from pages.Rent_page import Rent_page

@allure.description("test_buy_product")
def test_action(set_up):

    driver = webdriver.Chrome(ChromeDriverManager().install())
    # path_to_screenshot = "..\\screen\\"

    main_page = Main_page(driver)
    main_page.follow_to_rent_page()

    rent_page = Rent_page(driver)
    rent_page.send_application()

    time.sleep(2)
    driver.close()