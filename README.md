# Дипломный проект, задание №3 - UI тесты для покрытия сайта Stellar Burgers

## Используемые модули и библиотеки
Selenium - библиотека для взаимодействия с драйверами браузеров
Pytest - тестовый фреймворк
Allure - отчеты о тестировании

## Структура проекта
allure-results/ - результаты allure прогона
conftest.py - фикстуры
helper.py - вспомогательные классы
locators.py - локаторы
pages/ - классы страниц
README.md - данный файл
test_data.py - тестовые данные
tests/ - тесты

## Запуск автотестов
### Установка зависимостей

$ pip install -r requirements.txt

### Запуск автотестов и создание результов тестирования

$ python -m pytest --alluredir=allure-results

### Создание HTML-отчета на основании результатов тестирования

$ allure generate allure-results и $ allure open allure-report
 или 
$ allure serve allure-results
