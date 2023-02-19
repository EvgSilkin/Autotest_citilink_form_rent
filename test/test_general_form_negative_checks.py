import allure
from selenium.common import TimeoutException

from pages.Rent_page import Rent_page
from utilities.Logger import Logger

# Невозможность отправления заявки на сотрудничество, оставив все поля пустыми
@allure.description("test_case_3")
def test_case_3(driver):
    Logger.add_start_step(method="Невозможность отправления заявки на сотрудничество, оставив все поля пустыми")
    path_to_screenshot = "screen\\"

    form_marker = "Заявка на сотрудничество"
    errors_input_marker = "InputBox_error"
    rent_name = "name"
    errors_rent_name = "Поле должно содержать минимум 2 символа"
    rent_phone = "phone"
    errors_rent_phone = "Поле должно содержать 11 цифр"
    rent_mail = "email"
    errors_rent_mail = "Поле обязательно для заполнения"
    rent_city = "city"
    errors_rent_city = "Поле должно содержать минимум 2 символа"
    current_assert_input = ""

    rent_page = Rent_page(driver)
    rent_page.open_page()
    # Шаг 1. Нажать кнопку "Оставить заявку"
    rent_page.open_rent_form(form_marker)
    # Шаг 2.  Нажать на кнопку "Отправить предложение"
    rent_page.click_button_send_application()
    try:
        # ОР 1. "Ваше ФИО*": лейбл поля, нижняя граница поля ввода окрашены в красный цвет.
        current_assert_input = rent_name
        rent_page.assert_class_contains_str(current_assert_input, errors_input_marker)
        # ОР 2. Под полем ввода "Ваше ФИО*" отображается подсказка "Поле должно содержать минимум 2 символа"
        rent_page.assert_errors_input_message(current_assert_input, errors_rent_name)
        # ОР 3. "Контактный номер телефона*": лейбл поля, нижняя граница поля ввода окрашены в красный цвет.
        current_assert_input = rent_phone
        rent_page.assert_class_contains_str(current_assert_input, errors_input_marker)
        # ОР 4. Под полем ввода "Контактный номер телефона*" отображается подсказка "Поле должно содержать 11 цифра"
        rent_page.assert_errors_input_message(current_assert_input, errors_rent_phone)
        # ОР 5. "Email  для ответа*": лейбл поля, нижняя граница поля ввода окрашены в красный цвет.
        current_assert_input = rent_mail
        rent_page.assert_class_contains_str(current_assert_input, errors_input_marker)
        # ОР 6. Под полем ввода "Email  для ответа*" отображается подсказка "Поле обязательно для заполнения"
        current_assert_input = rent_mail
        rent_page.assert_errors_input_message(current_assert_input, errors_rent_mail)
        # ОР 7. "Введите город и область*": лейбл поля, нижняя граница поля ввода окрашены в красный цвет.
        current_assert_input = rent_city
        rent_page.assert_class_contains_str(current_assert_input, errors_input_marker+"")
        # ОР 8. Под полем ввода "Введите город и область*" отображается подсказка "Поле должно содержать минимум 2 символа"
        rent_page.assert_errors_input_message(current_assert_input, errors_rent_city)
    except AssertionError:
        print(f"Нижняя граница поля ввода rent_{current_assert_input} не окрашена в красный цвет или "
              f"Неверное сообщение об ошибке для поля rent_{current_assert_input}")
        raise AssertionError(f"Нижняя граница поля ввода rent_{current_assert_input} не окрашена в красный цвет или "
              f"Неверное сообщение об ошибке для поля rent_{current_assert_input}")
    except TimeoutException:
        print(f"Ошибка 'Timeout' поиска элемента rent_{current_assert_input}")
        raise AssertionError(f"Ошибка 'Timeout' поиска элемента rent_{current_assert_input}")
    finally:
        rent_page.screen_page(path_to_screenshot)
        Logger.add_end_step(url=rent_page.get_current_url(),
                            method="Невозможность отправления заявки на сотрудничество, оставив все поля пустыми")

