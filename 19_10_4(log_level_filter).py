from typing import Generator

def log_filter(logs: str, level: str) -> Generator[str, None, None]:
    for line in logs.splitlines():
        if f" {level} " in line:  # Проверка на заданный уровень логирования
            yield line
logs = """\
2023-08-15 14:15:24 INFO Starting the system.
2023-08-15 14:15:26 WARN System load is above 80%.
2023-08-15 14:15:27 ERROR Failed to connect to database.
2023-08-15 14:15:28 INFO Connection retry in 5 seconds.
"""

to_test = list(log_filter(logs, level="ERROR"))
print(to_test)
# Ожидаемый вывод:
# ['2023-08-15 14:15:27 ERROR Failed to connect to database.']
