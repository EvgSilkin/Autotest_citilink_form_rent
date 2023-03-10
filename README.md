### В этом репозитории расположен проект-портфолио по автоматизации тестирования UI-компонента интернет-магазина «[Ситилинк](https://www.citilink.ru/rent/)» — форма оформления «Заявки на сотрудничество» и аренды помещения.

#### Проект реализован на языке программирования Python.
#### В проекте задействованы следующие пакеты (и их зависимости):
- selenium
- pytest
- pytest-order
- webdriver-manager
- allure

Проверки, выполняемые в этом проекте, основаны на ранее мной составленных проверках, для выполнения ручного тестирования формы.
Составленные проверки можно посмотреть по ссылке: [Ссылка на проверки](https://docs.google.com/spreadsheets/d/1X5DfJBz8_889Zj-2zQD4egbdoxDBBPHvtp0Zu1kLZD0/edit#gid=1272824100 "Проверка функционала формы \"Заявка на сотрудничество\" Больше 150 М2")
Из списка выше(по ссылке) для демонстрации в программе реализованы Тест-Кейсы под номерами 1, 2, 3, 4, 48, 49 и 50.

[Ссылка на портфолио](https://docs.google.com/document/d/1qqiY6eE5F0_nukb1E979TQb4SeIlW6y7y4AQ6zcDu28/edit "QA Engineer | Тестировщик – Силкин Евгений")

---
# ВАЖНО!!!

При выполнении позитивных проверок из файла `test_general_form_positive_checks.py` необходимо учесть особенность тестирования формы.
При выполнении позитивных проверок с названием методов `test_sending_application_by_filling_all_fields_valid_data` и `test_sending_application_by_filling_all_required_fields_valid_data` для получения ожидаемого результат требуется ручное вмешательство.
При запуске указанных выше проверок с помощью автоматизированного тестового ПО форма требует ввода *капчи*. В коде искусственно задано ожидание на 7 секунд, после заполнения всей формы, чтобы тестировщик успел ввести капчу.

---

#### Подключение и настройка проекта на локальном компьютере:
- Клонировать проект на локальный компьютер

#### При необходимости установки пакетов и зависимостей:
- Создать виртуальное окружение:
_File - Settings - Project: name - Python Interpreter - Add interpreter_
- Перейти в виртуальное окружение с помощью ввода в терминале команды: `venv/Scripts/activate`
- Установить пакеты и зависимости с помощью ввода в терминал команды: `pip install -r requirements.txt`

#### Команды для работы с проектом:
- Запустить тест с помощью ввода в терминал команды: `python -m pytest --alluredir=test_results/ test/`
- Отобразить allure-отчет, после выполнения проверок с помощью ввода в терминал команды: `allure serve test_results/`


