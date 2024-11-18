def find_duplicates(arr):
  # Инициализация множества для уникальных элементов и списка для дубликатов.
  seen = set()
  duplicates = []
  for item in arr:
    # Если элемент уже встречался, добавить в дубликаты.
    if item in seen:
      duplicates.append(item)
    else:
      # Иначе добавить в уникальные элементы.
      seen.add(item)
  # Возвращение списка дубликатов.
  return duplicates