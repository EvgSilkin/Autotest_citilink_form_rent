import time
import allure

from selenium.common import TimeoutException
from pages.Rent_page import Rent_page
from utilities.Logger import Logger


# Отправление заявки на сотрудничество, заполнив все поля валидными данными
@allure.description("test_case_1")
def test_case_1(driver):
    Logger.add_start_step(method="Отправление заявки на сотрудничество, заполнив все поля валидными данными")
    path_to_screenshot = "screen\\"
    form_marker = "Заявка на сотрудничество"
    text_marker = "Спасибо за заявку на сотрудничество"
    rent_name = "Иванов Иван Иванович"
    rent_phone = "9123456789"
    rent_mail = "test@test.ru"
    rent_city = "Казань Татарстан"
    rent_description = "Цокольный этаж"

    rent_page = Rent_page(driver)
    rent_page.open_page()
    # Шаг 1. Нажать кнопку "Оставить заявку"
    rent_page.open_rent_form(form_marker)
    # Шаг 2. Ввести в поле "Ваше ФИО*" значение: "Иванов Иван Иванович"
    rent_page.fill_input_rent_name(rent_name)
    # Шаг 3. Ввести в поле "Контактный номер телефона*" значение: "+79123456789"
    rent_page.fill_input_rent_phone(rent_phone)
    # Шаг 4. Ввести в поле "Email для ответа*" значение: "test@test.ru"
    rent_page.fill_input_rent_mail(rent_mail)
    # Шаг 5. Ввести в поле "Введите город и область*" значение: "Казань Татарстан"
    rent_page.fill_input_rent_city(rent_city)
    # Шаг 6. Ввести в поле "Опишите особенности помещения" значение: "Цокольный этаж"
    rent_page.fill_input_rent_description(rent_description)
    time.sleep(7)
    try:
        # Шаг 7. Примечание: Опциональный шаг. Ввода капчи требуется не при каждом оформлении заявки на сотрудничесво.
        # Ввести(в ручную) в поле "Слово с картинки*" значенние капчи
        # Шаг 8.  Нажать на кнопку "Отправить предложение"
        rent_page.send_application(text_marker)
    except TimeoutException:
        raise TimeoutException("Не найден маркер успешного завершения проверки test_case_1")
    finally:
        rent_page.screen_page(path_to_screenshot)
        Logger.add_end_step(url=rent_page.get_current_url(),
                            method="Отправление заявки на сотрудничество,"
                                   " заполнив все поля валидными данными")

# Отправление заявки на сотрудничество, заполнив все обязательные поля валидными данными
@allure.description("test_case_2")
def test_case_2(driver):
    Logger.add_start_step(method="Отправление заявки на сотрудничество, "
                                 "заполнив все обязательные поля валидными данными")
    path_to_screenshot = "screen\\"
    form_marker = "Заявка на сотрудничество"
    text_marker = "Спасибо за заявку на сотрудничество"
    rent_name = "Иванов Иван Иванович"
    rent_phone = "9123456789"
    rent_mail = "test@test.ru"
    rent_city = "Казань Татарстан"

    rent_page = Rent_page(driver)
    rent_page.open_page()
    # Шаг 1. Нажать кнопку "Оставить заявку"
    rent_page.open_rent_form(form_marker)
    # Шаг 2. Ввести в поле "Ваше ФИО*" значение: "Иванов Иван Иванович""
    rent_page.fill_input_rent_name(rent_name)
    # Шаг 3. Ввести в поле "Контактный номер телефона*" значение: "+79123456789""
    rent_page.fill_input_rent_phone(rent_phone)
    # Шаг 4. Ввести в поле "Email для ответа*" значение: "test@test.ru""
    rent_page.fill_input_rent_mail(rent_mail)
    # Шаг 5. Ввести в поле "Введите город и область*" значение: "Казань Татарстан""
    rent_page.fill_input_rent_city(rent_city)
    time.sleep(7)
    try:
        # Шаг 6. Примечание: Опциональный шаг. Ввода капчи требуется не при каждом оформлении заявки на сотрудничесво.
        # Ввести(в ручную) в поле "Слово с картинки*" значенние капчи
        # Шаг 7.  Нажать на кнопку "Отправить предложение"
        rent_page.send_application(text_marker)
    except TimeoutException:
        raise TimeoutException("Не найден маркер успешного завершения проверки test_case_2")
    finally:
        rent_page.screen_page(path_to_screenshot)
        Logger.add_end_step(url=rent_page.get_current_url(),
                            method="Отправление заявки на сотрудничество, "
                                   "заполнив все обязательные поля валидными данными")

# Сохранение заполненных данных в форме, после изменения выбранной площади
@allure.description("test_case_48")
def test_case_48(driver):
    Logger.add_start_step(method="Сохранение заполненных данных в форме, после изменения выбранной площади")
    path_to_screenshot = "screen\\"
    value_for_assert = "RentFeedback____inner feedback-radio feedback-radio-less active"
    form_marker = "Заявка на сотрудничество"
    rent_name = "Иванов Иван Иванович"
    rent_phone = "9123456789"
    rent_mail = "test@test.ru"
    rent_city = "Казань Татарстан"
    rent_description = "Цокольный этаж"
    current_assert_input = ""

    rent_page = Rent_page(driver)
    rent_page.open_page()
    # Шаг 1. Нажать кнопку "Оставить заявку"
    rent_page.open_rent_form(form_marker)
    # Шаг 2. Ввести в поле "Ваше ФИО*" значение: "Иванов Иван Иванович""
    rent_page.fill_input_rent_name(rent_name)
    # Шаг 3. Ввести в поле "Контактный номер телефона*" значение: "+79123456789"
    rent_page.fill_input_rent_phone(rent_phone)
    # Шаг 4. Ввести в поле "Email для ответа*" значение: "test@test.ru"
    rent_page.fill_input_rent_mail(rent_mail)
    # Шаг 5. Ввести в поле "Введите город и область*" значение: "Казань Татарстан"
    rent_page.fill_input_rent_city(rent_city)
    # Шаг 6. Ввести в поле "Опишите особенности помещения" значение: "Цокольный этаж"
    rent_page.fill_input_rent_description(rent_description)
    # Шаг 7. Нажать на таб-кнопку "Меньше 40М2"
    rent_page.change_form_to_area_less_40_metres(value_for_assert)
    try:
        # ОР 1:  Сохранились заполненные значения для поля: "Ваше ФИО*"
        current_assert_input = "rent_name"
        rent_page.get_and_assert_input_value(current_assert_input, rent_name)
        # ОР 2:  Сохранились заполненные значения для поля: "Контактный номер телефона*"
        current_assert_input = "rent_phone"
        rent_page.get_and_assert_input_value(current_assert_input, rent_phone)
        # ОР 3:  Сохранились заполненные значения для поля: "Введите город и область*"
        current_assert_input = "rent_city"
        rent_page.get_and_assert_input_value(current_assert_input, rent_city+"test")
    except AssertionError:
        print(f"Ошибка при проверки поля {current_assert_input}")
        raise AssertionError(f"Ошибка при проверки поля {current_assert_input}")
    finally:
        rent_page.screen_page(path_to_screenshot)
        Logger.add_end_step(url=rent_page.get_current_url(), method="Сохранение заполненных данных в форме,"
                                                                  "после изменения выбранной площади")
# Сохранение заполненных данных в форме, после возврата на изначальную площадь
@allure.description("test_case_49")
def test_case_49(driver):
    Logger.add_start_step(method="Сохранение заполненных данных в форме, после возврата на изначальную площадь")
    path_to_screenshot = "screen\\"
    value_for_assert_less_40 = "RentFeedback____inner feedback-radio feedback-radio-less active"
    value_for_assert_more_150 = "RentFeedback____inner feedback-radio feedback-radio-more active"
    form_marker = "Заявка на сотрудничество"
    rent_name = "Иванов Иван Иванович"
    rent_phone = "9123456789"
    rent_mail = "test@test.ru"
    rent_city = "Казань Татарстан"
    rent_description = "Цокольный этаж"
    current_assert_input = ""

    rent_page = Rent_page(driver)
    rent_page.open_page()
    # Шаг 1. Нажать кнопку "Оставить заявку"
    rent_page.open_rent_form(form_marker)
    # Шаг 2. Ввести в поле "Ваше ФИО*" значение: "Иванов Иван Иванович""
    rent_page.fill_input_rent_name(rent_name)
    # Шаг 3. Ввести в поле "Контактный номер телефона*" значение: "+79123456789"
    rent_page.fill_input_rent_phone(rent_phone)
    # Шаг 4. Ввести в поле "Email для ответа*" значение: "test@test.ru"
    rent_page.fill_input_rent_mail(rent_mail)
    # Шаг 5. Ввести в поле "Введите город и область*" значение: "Казань Татарстан"
    rent_page.fill_input_rent_city(rent_city)
    # Шаг 6. Ввести в поле "Опишите особенности помещения" значение: "Цокольный этаж"
    rent_page.fill_input_rent_description(rent_description)
    # Шаг 7. Нажать на таб-кнопку "Меньше 40М2"
    rent_page.change_form_to_area_less_40_metres(value_for_assert_less_40)
    # Шаг 8. Нажать на таб-кнопку "Больше 150М2"
    rent_page.change_form_to_area_more_150_metres(value_for_assert_more_150)
    try:
        # ОР 1:  Сохранились заполненное значение для поля: "Ваше ФИО*"
        current_assert_input = "rent_name"
        rent_page.get_and_assert_input_value("rent_name", rent_name)
        # ОР 2:  Сохранилось заполненное значение для поля: "Контактный номер телефона*"
        current_assert_input = "rent_phone"
        rent_page.get_and_assert_input_value("rent_phone", rent_phone)
        # ОР 3:  Сохранилось заполненное значение для поля: "Введите город и область*"
        current_assert_input = "rent_city"
        rent_page.get_and_assert_input_value("rent_city", rent_city)
        # ОР 4:  Сохранилось заполненное значение для поля: "Email для ответа*"
        current_assert_input = "rent_mail"
        rent_page.get_and_assert_input_value("rent_mail", rent_mail)
        # ОР 5:  Сохранилось заполненное значение для поля: "Опишите особенности помещения"
        current_assert_input = "rent_description"
        rent_page.get_and_assert_input_value(current_assert_input, rent_description)
    except AssertionError:
        print(f"Ошибка при проверки поля {current_assert_input}")
        raise AssertionError(f"Ошибка при проверки поля {current_assert_input}")
    finally:
        rent_page.screen_page(path_to_screenshot)
        Logger.add_end_step(url=rent_page.get_current_url(), method="Сохранение заполненных данных в форме, "
                                                                    "после возврата на изначальную площадь")
# Сохранение заполненных данных в форме, после закрытия формы
@allure.description("test_case_50")
def test_case_50(driver):
    Logger.add_start_step(method="Сохранение заполненных данных в форме, после закрытия формы")
    path_to_screenshot = "screen\\"
    form_marker = "Заявка на сотрудничество"
    rent_name = "Иванов Иван Иванович"
    rent_phone = "9123456789"
    rent_mail = "test@test.ru"
    rent_city = "Казань Татарстан"
    rent_description = "Цокольный этаж"
    current_assert_input = ""

    rent_page = Rent_page(driver)
    rent_page.open_page()
    # Шаг 1. Нажать кнопку "Оставить заявку"
    rent_page.open_rent_form(form_marker)
    # Шаг 2. Ввести в поле "Ваше ФИО*" значение: "Иванов Иван Иванович""
    rent_page.fill_input_rent_name(rent_name)
    # Шаг 3. Ввести в поле "Контактный номер телефона*" значение: "+79123456789"
    rent_page.fill_input_rent_phone(rent_phone)
    # Шаг 4. Ввести в поле "Email для ответа*" значение: "test@test.ru"
    rent_page.fill_input_rent_mail(rent_mail)
    # Шаг 5. Ввести в поле "Введите город и область*" значение: "Казань Татарстан"
    rent_page.fill_input_rent_city(rent_city)
    # Шаг 6. Ввести в поле "Опишите особенности помещения" значение: "Цокольный этаж"
    rent_page.fill_input_rent_description(rent_description)
    # Шаг 7. Закрыть форму заполнения заявки
    rent_page.close_rent_form()
    # Шаг 8. Нажать кнопку "Оставить заявку"
    rent_page.open_rent_form(form_marker)
    try:
        # ОР 1:  Сохранились заполненное значение для поля: "Ваше ФИО*"
        current_assert_input = "rent_name"
        rent_page.get_and_assert_input_value("rent_name", rent_name)
        # ОР 2:  Сохранилось заполненное значение для поля: "Контактный номер телефона*"
        current_assert_input = "rent_phone"
        rent_page.get_and_assert_input_value("rent_phone", rent_phone)
        # ОР 3:  Сохранилось заполненное значение для поля: "Введите город и область*"
        current_assert_input = "rent_city"
        rent_page.get_and_assert_input_value("rent_city", rent_city)
        # ОР 4:  Сохранилось заполненное значение для поля: "Email для ответа*"
        current_assert_input = "rent_mail"
        rent_page.get_and_assert_input_value("rent_mail", rent_mail)
        # ОР 4:  Сохранилось заполненное значение для поля: "Опишите особенности помещения"
        current_assert_input = "rent_description"
        rent_page.get_and_assert_input_value("rent_description", rent_description)
    except AssertionError:
        print(f"Ошибка при проверки поля {current_assert_input}")
        raise AssertionError(f"Ошибка при проверки поля {current_assert_input}")
    finally:
        rent_page.screen_page(path_to_screenshot)
        Logger.add_end_step(url=rent_page.get_current_url(), method="Сохранение заполненных данных в форме, "
                                                                    "после закрытия формы")
