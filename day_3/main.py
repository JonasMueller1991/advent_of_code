import string
from itertools import islice
from typing import List

from more_itertools import strip

map_value = dict()
for index, letter in enumerate(string.ascii_lowercase):
    map_value[letter] = index + 1
for index, letter in enumerate(string.ascii_uppercase):
    map_value[letter] = index + 27


def get_priority(item: str):
    return map_value[item]


def find_failing_type(pack_list: str):
    slicing_index = int(len(pack_list) / 2)
    full_first_compartment = pack_list[:slicing_index]
    full_second_compartment = pack_list[slicing_index:]

    first_compartment = set(c for c in full_first_compartment)
    second_compartment = set(c for c in full_second_compartment)

    for item in first_compartment:
        if item in second_compartment:
            return item


def part_1():
    sum_priority = 0
    with open('rucksack.csv') as file:
        for line in file:
            item = find_failing_type(line)
            sum_priority += get_priority(item)
    print(f'Sum of priorities: {sum_priority}')


def get_elve_groups(group_size: int):
    with open('rucksack.csv', 'r') as file:
        while True:
            lines = list(islice(file, group_size))
            if lines:
                yield [c.strip() for c in lines]
            else:
                break


def find_badge(elve_group: List[str]):
    set_group = [set(group) for group in elve_group]
    elements_of_two_elves = set_group[1] & set_group[2]
    for item in set_group[0]:
        if item in elements_of_two_elves:
            return item


def part_2():
    sum_priorities = 0
    for group in get_elve_groups(group_size=3):
        sum_priorities += get_priority(find_badge(group))
    print(f'Sum of priorities: {sum_priorities}')


if __name__ == '__main__':
    # part_1()
    part_2()
