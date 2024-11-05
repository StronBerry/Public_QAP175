from typing import Dict, List


def extract_categories(categories: Dict[str, Dict], parent_path: str = '') -> List[str]:
    paths = []
    for category, subcategories in categories.items():
        # Формируем полный путь для текущей категории
        current_path = f"{parent_path} > {category}" if parent_path else category
        paths.append(current_path)  # Добавляем текущий путь в список

        # Если у текущей категории есть подкатегории, рекурсивно вызываем функцию
        if subcategories:
            paths.extend(extract_categories(subcategories, current_path))

    return paths
categories = {
   "Электроника": {
       "Телефоны": {
           "Смартфоны": {},
           "Проводные": {}
       },
       "Компьютеры": {
           "Ноутбуки": {},
           "Стационарные": {
               "Игровые": {},
               "Для работы": {}
           }
       }
   },
   "Одежда": {
       "Мужская": {
           "Джинсы": {},
           "Куртки": {}
       }
   }
}

# Вызов функции без передачи родительского пути
paths = extract_categories(categories)
for path in paths:
    print(path)

# Вызов функции с передачей родительского пути
print("\nWith parent path:")
paths_with_root = extract_categories(categories, parent_path='root')
for path in paths_with_root:
    print(path)
