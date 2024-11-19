class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

from collections import deque
def breadth_first_search_for_files(root, target_name):
    """
    Выполняет поиск файлов с именем target_name в дереве файловой системы, используя обход в ширину.

    :param root: корневой узел дерева (TreeNode)
    :param target_name: имя файла для поиска
    :return: список путей, где найден файл
    """
    result = []  # Для хранения найденных путей
    queue = deque([(root, root.name)])  # Очередь узлов: (текущий узел, текущий путь)

    while queue:
        current_node, current_path = queue.popleft()

        # Проверяем, совпадает ли имя файла
        if current_node.name == target_name:
            result.append(current_path)

        # Добавляем всех детей в очередь
        for child in current_node.children:
            queue.append((child, f"{current_path}/{child.name}"))

    return result

root = TreeNode("C:")

root.add_child(TreeNode("Summary.docx"))

documents = TreeNode("Documents")
root.add_child(documents)
documents.add_child(TreeNode("Homework.docx"))
documents.add_child(TreeNode("Report.docx"))
documents.add_child(TreeNode("Summary.docx"))

pictures = TreeNode("Pictures")
root.add_child(pictures)
pictures.add_child(TreeNode("Summer.jpg"))
pictures.add_child(TreeNode("Winter.jpg"))
pictures.add_child(TreeNode("Summary.docx"))

file_paths = breadth_first_search_for_files(root, 'Summary.docx')
for file_path in file_paths:
    print(file_path[:-1])


