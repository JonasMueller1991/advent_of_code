from dataclasses import dataclass, field
from itertools import takewhile
from typing import List


def get_tree_array():
    tree_array = []
    with open('input.csv', 'r') as file_input:
        for line_input in file_input:
            tree_array.append([int(num) for num in line_input.strip()])
    return tree_array, len(tree_array), len(tree_array[0])


def check_row(tree_row: List[int]) -> List[bool]:
    current_max_height = -1  # First and last trees are always visible
    visible = []
    for tree in tree_row:
        if tree > current_max_height:
            current_max_height = tree
            visible.append(True)
        else:
            visible.append(False)
    return visible


def get_reversed_list(input_list: List):
    return_list = input_list.copy()
    return_list.reverse()
    return return_list


def get_top_view(input_list: List[List]) -> List[List]:
    x_dim = len(input_list)
    y_dim = len(input_list[0])
    return [[input_list[x][y] for x in range(y_dim)] for y in range(x_dim)]


def check_row_in_different_direction(row: List[int]) -> List[bool]:
    return get_reversed_list(check_row(get_reversed_list(row)))


@dataclass
class Tree:
    x: int
    y: int
    tree_heights: List[List[int]]
    x_dim: int = field(init=False)
    y_dim: int = field(init=False)
    tree_height: int = field(init=False)
    view_right: List[int] = field(init=False)
    view_top: List[int] = field(init=False)
    view_bottom: List[int] = field(init=False)
    view_left: List[int] = field(init=False)

    def __post_init__(self):
        self.x_dim = len(self.tree_heights)
        self.y_dim = len(self.tree_heights[0])
        self.tree_height = self.tree_heights[self.x][self.y]

        if self.y == 0:
            self.view_left = []
        else:
            self.view_left = get_reversed_list(
                [self.tree_heights[self.x][view_index] for view_index in range(0, self.y)])
        if self.x == 0:
            self.view_top = []
        else:
            self.view_top = get_reversed_list(
                [self.tree_heights[view_index][self.y] for view_index in range(0, self.x)])
        if self.x == x_dim:
            self.view_bottom = []
        else:
            self.view_bottom = [self.tree_heights[view_index][self.y] for view_index in range(self.x + 1, self.x_dim)]

        if self.y == y_dim:
            self.view_right = []
        else:
            self.view_right = [self.tree_heights[self.x][view_index] for view_index in range(self.y + 1, self.y_dim)]

    def count_visible_trees_in_view(self, view: List[int]) -> int:
        view_counter = 0
        for view_height in view:
            view_counter += 1
            if view_height >= self.tree_height:
                return view_counter
        return view_counter

    def calc_scenic_score(self):
        left_scenic_factor = self.count_visible_trees_in_view(self.view_left)
        right_scenic_factor = self.count_visible_trees_in_view(self.view_right)
        top_scenic_factor = self.count_visible_trees_in_view(self.view_top)
        bottom_scenic_factor = self.count_visible_trees_in_view(self.view_bottom)
        return left_scenic_factor * right_scenic_factor * top_scenic_factor * bottom_scenic_factor


def part_1():
    global tree_heights, x_dim, y_dim
    tree_heights, x_dim, y_dim = get_tree_array()
    # row wise
    left_visible = []
    right_visible = []
    transformed_top_visible = []
    top_visible = []
    transformed_bottom_visible = []
    bottom_visible = []
    for row in tree_heights:
        left_visible.append(check_row(row))
    right_visible.append(check_row_in_different_direction(row))
    for row in get_top_view(tree_heights):
        transformed_top_visible.append(check_row(row))
    transformed_bottom_visible.append(check_row_in_different_direction(row))
    top_visible = get_top_view(transformed_top_visible)
    bottom_visible = get_top_view(transformed_bottom_visible)
    visible = [[None for _ in range(x_dim)] for _ in range(y_dim)]
    counter = 0
    for id_x in range(x_dim):
        for id_y in range(y_dim):
            if left_visible[id_x][id_y] or right_visible[id_x][id_y] or top_visible[id_x][id_y] or bottom_visible[id_x][
                id_y]:
                counter += 1
    print(f'Count of visible trees: {counter}')


def part_2():
    global x_dim, y_dim
    trees, x_dim, y_dim = get_tree_array()
    view_scores = []
    for i in range(0, x_dim):
        for j in range(0, y_dim):
            view_scores.append(Tree(i, j, tree_heights=trees).calc_scenic_score())
    print(f'Highest scenic score is: {max(view_scores)}')


if __name__ == '__main__':
    part_2()
