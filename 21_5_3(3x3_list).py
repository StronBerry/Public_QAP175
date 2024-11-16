class AreaPoint:
    def __init__(self, i: int, j: int, height: int = 15):
        self.i = i
        self.j = j
        self.height = height

# Создание двумерного списка area_list размером 3 x 3
area_list = [[AreaPoint(i, j) for i in range(3)] for j in range(3)]


len_area_list = len(area_list)
print(len_area_list)

check_area_list = [[isinstance(elem, AreaPoint) for elem in row] for row in area_list]
print(check_area_list)

area_list_coordinates = [[(elem.i, elem.j) for elem in row] for row in area_list]
print(area_list_coordinates)

area_point = AreaPoint(10, 13)
print(area_point.height)

area_point = AreaPoint(10, 13, height=180)
print(area_point.height)

# 3
# [[True, True, True], [True, True, True], [True, True, True]]
# [[(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)]]
# 15
# 180