import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import Workbook
from bs4 import BeautifulSoup

driver = webdriver.Chrome() # Инициализация WebDriver


def get_data(url):
    driver.get(url)

    time.sleep(5)  # Таймер ожидания, чтобы страница полностью загрузилась

    page_source = driver.page_source     # HTML код страницы после отработки всех скриптов
    soup = BeautifulSoup(page_source, 'html.parser')
    data = [] # Список хранения собранных данных

    tasks = soup.find_all('h2', class_='text-xl font-bold') # Поиск блоков с названиями (именами) заданий


    if not tasks:
        print("Не удалось найти нужные данные на странице.")
        return [] # Проверка, что блоки с названиями (именами) заданий найдены


    percentages = soup.find_all('div', class_='font-bold text-sm') # Поиск блоков с процентами лайков и дизлайков

    if len(tasks) != len(percentages) // 2: # Если количество "Задание + процентная пара" не совпадает, выводится предупреждение
        print(
            f"Внимание! Количество заданий и процентов не совпадает. Заданий: {len(tasks)}, процентов: {len(percentages) // 2}")


    for i, task in enumerate(tasks): # Перебор найденных блоков названий и процентов
        task_name = task.get_text(strip=True)
        try: # Извлечение процента лайков и дизлайков, если они присутствуют
            like_percentage = percentages[i * 2].get_text(strip=True).replace('%', '')
            dislike_percentage = percentages[i * 2 + 1].get_text(strip=True).replace('%', '')
        except IndexError:
            like_percentage = ''
            dislike_percentage = ''
        if not like_percentage or not dislike_percentage: # Пропуск строк, если данные пустые
            continue
        data.append([task_name, like_percentage, dislike_percentage]) # Добавление данных в список
    return data


def save_to_excel(data, filename): # Сохранение данных в файл .xlsx
    if not data:
        print("Нет данных для сохранения.")
        return
    wb = Workbook()
    ws = wb.active
    ws.title = "SBC Data"
    ws.append(["Имя задания", "Лайки (%)", "Дизлайки (%)"])

    for row in data: # Оформление данных в таблицу
        ws.append(row)

    wb.save(filename) # Сохранение файла
    print(f"Данные успешно сохранены в файл: {filename}")


# Инициализатор парсера

if __name__ == "__main__":
    url = "https://www.fut.gg/sbc/"
    data = get_data(url)

    if data:
        save_to_excel(data, "sbc_data.xlsx")  # Сохранение "sbc_data.xlsx"
    else:
        print("Данные не были собраны.")

    driver.quit() # Закрытие браузера
