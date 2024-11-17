class TaskList:
    def __init__(self):
        self.__task_list = []  # Приватный список задач

    def __is_task_in_list(self, task_name):
        """Проверяет, существует ли задача с именем task_name в списке."""
        return any(task['name'] == task_name for task in self.__task_list)

    def add_task(self, task_name):
        """Добавляет задачу в список, если её ещё нет."""
        if self.__is_task_in_list(task_name):
            print(f'Задача "{task_name}" уже есть в списке')
        else:
            self.__task_list.append({'name': task_name, 'done': False})
            print(f'Задача "{task_name}" добавлена в список')

    def remove_task(self, task_name):
        """Удаляет задачу с именем task_name из списка, если она существует."""
        if self.__is_task_in_list(task_name):
            self.__task_list = [task for task in self.__task_list if task['name'] != task_name]
            print(f'Задача "{task_name}" удалена из списка')
        else:
            print(f'Задачи "{task_name}" нет в списке')

# Пример использования:
ts = TaskList()

# Добавляем задачи
ts.add_task('Create get_task_list() method')
ts.add_task('Show students how __task_list attr looks like')
ts.add_task('Show students how __task_list attr looks like')  # Повторная добавка

# Удаляем задачу
ts.add_task('Show students how work remove_task() method')
ts.remove_task('Show students how work remove_task() method')

# Смотрим приватный список задач
print(ts._TaskList__task_list)
