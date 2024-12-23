Парсер оценок пользователей для серивиса fut.gg

1. Функционал сайта fut.gg являет собой стороннее дополнение и базу данных для режима онлайн игры FC25 (EA Sports). Сайт входит в тройку тематических сайтов по количеству активных пользователей за 2020-2023 гг.
2. Данный парсер принимает данные со страницы https://www.fut.gg/sbc/, на которой размещена информация об испытаниях, которые пользователи могут выполнить в процессе игры. Важным дополнением является наличие оценок (лайков и дизлайков) зарегистрированных пользователей сайта, так как функционал оценок пользователей полностью отсутствует непосредственно в интерфейсе игры.
3. Основная задача - корректный сбор информации о названиях (именах) испытаний, процентном соотношении лайков и дизлайков, вывод итоговых данных в таблицу формата .xlsx
4. Оценка или кросс-корреляция итоговых данных работы парсера в первую очередь направлена на анализ пользовательского опыта при взаимодействии с отдельными элементами игры FC25 (EA Sports).
5. Принцип работы парсера может быть экспонирован на другие разделы сайта, так как большинство разделов имеют схожий структурный принцип: Объект + процентное соотношение отношения пользователей.


Шаги написания кода парсера:
1. Обращение и загрузка html-кода страницы
2. Извлечение названий (имен) объектов
3. Извлечение данных о процентах лайков и дизлайков - на этом этапе стало очевидно, что эти данные являются динамическими (JS) и не отображаются в текстом изложении кода страницы.
4. Поиск решения в интернете подсказал реализацию парсинга через модуль Selenium + Google Driver
5. Отказ от пункта 1 и 2 в пользу извлечений данных одним способом.
6. Формирование таблицы из списков полученных данных
7. Сохранение данных в виде файла .xlsx

(Не очень понимаю, что такое - инструкция к запуску кода)

Результат данных на 24.11.2024 находится в таблице sbc_data.xlsx