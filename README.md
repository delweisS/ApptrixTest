# CryptocurrencyApp

![Crypto](https://i.ibb.co/gSGqYTn/2023-03-17-14-48-19.png)

## Описание

Тестовое задание для компании Apptrix. Готовое решение можно протестировать на [PythonAnywhere](http://yosun.pythonanywhere.com/).
  
**Задание:** Необходимо разработать веб-приложение, которое будет использовать API для получения данных о курсах криптовалют (например, от CoinMarketCap или Coinbase). 

## Основные функции

Согласно условиям задачи, было реализовано:

* Вывод информации о криптовалютах (используется [CoinMarketCap API](https://coinmarketcap.com/));
* Поиск криптовалют по названию или символьному коду;
* Возможность добавления криптовалют в список избранных, отображение списка избранных криптовалют;
* Вывод новостей на тему криптовалют (используется [NewsAPI](https://newsapi.org/));
* Авторизация и регистрация пользователей, хранение данных в базе данных;

Создано REST API, реализующее следующие задачи:

* Получение списка всех криптовалют;
* Получение информации о конкретной криптовалюте по символьному коду;
* Добавление новой криптовалюты;
* Обновление информации о криптовалюте;
* Удаление криптовалюты;
* Unit-tests с использованием pytest для тестирования всех методов API;

Также приложение развернуто на хостинге PythonAnywhere.

## Установка

Склонируйте репозиторий:
```
$ git clone https://gitlab.com/test-tasks9135311/apptrix-test.git
```
Создайте виртуальное окружение:
```
$ python -m venv .venv
```
Активируйте окружение:
```
$ source .venv/bin/activate
```
Загрузите пакеты из requirements.txt:
```
$ pip install -r requirements.txt
```
Запустите миграции:
```
$ python manage.py migrate
```
Создайте супер-пользователя:
```
$ python manage.py createsuperuser
```
Запустите тестовый сервер Django:
```
$ python manage.py runserver
```

## Тесты

Для тестирования используется фреймворк pytest.
Запустите тесты с помощью:
```
$ pytest
```