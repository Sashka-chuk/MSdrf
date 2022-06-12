Юхимчук Александр

Цель:
Реализовать сервис, который принимает и отвечает на HTTP запросы.

Инструменты:
● Фреймворк для обработки http запросов Django + Django Rest Framework
● БД PostgreSQL 
● Запросы в базу данных через ORM (ORM на выбор)
Объекты:
Магазин:
● Название
● Город
● Улица
● Дом
● Время открытия
● Время закрытия
Город:
● Название
Улица:
● Название
● Город

Функционал:
1. В случае успешной обработки сервис должен отвечать статусом 200, в
случае любой ошибки — статус 400.
2. Сохранение всех объектов в базе данных.
3. Запросы:
a. GET /city/ — получение списка городов из базы;
b. GET /city/city_id/street/ — получение списка улиц города (city_id —
идентификатор города);
c. POST /shop/ — создание магазина; Данный метод получает json c
объектом магазина, в ответ возвращает id созданной записи.
d. GET /shop/?street=&city=&open=0/1 — получение списка магазинов;
определяется исходя из параметров «Время открытия»,
«Время закрытия» и текущего времени сервера.
4. Ответы запросов должны быть в json формате.
