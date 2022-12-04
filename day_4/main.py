from typing import List


def get_assigned_ids(input_line: str) -> List[List]:
    assigned_ids = input_line.split(',')
    return_value = [[int(i.strip()) for i in cleaning_id.split('-')] for cleaning_id in assigned_ids]
    return return_value[0], return_value[1]


def check_input(a):
    if a[0] > a[1]:
        raise ValueError("Range is not ordered!")


def check_a_contains_b(a: List, b: List) -> bool:
    check_input(a)
    check_input(b)
    return a[0] <= b[0] and a[1] >= b[1]


def check_overlap(a: List, b: List) -> bool:
    return a[0] <= b[0] <= a[1] or a[0] <= b[1] <= a[1] or check_a_contains_b(b, a)


def check_assignment_for_containment(a: List, b: List) -> int:
    if check_a_contains_b(a, b) or check_a_contains_b(b, a):
        return 1
    else:
        return 0


def check_assignment_for_overlap(a: List, b: List) -> int:
    if check_overlap(a, b):
        return 1
    else:
        return 0


if __name__ == '__main__':
    result_sum_containment = 0
    result_sum_overlap = 0
    with open('input.csv', 'r') as file:
        for line in file:
            id_1, id_2 = get_assigned_ids(input_line=line)
            result_sum_containment += check_assignment_for_containment(id_1, id_2)
            result_sum_overlap += check_assignment_for_overlap(id_1, id_2)
    print(f'Containment result: {result_sum_containment}')
    print(f'Overlap result: {result_sum_overlap}')
