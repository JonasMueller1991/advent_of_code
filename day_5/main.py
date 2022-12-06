stacks = [
    ['W', 'B', 'D', 'N', 'C', 'F', 'J'],
    ['P', 'Z', 'V', 'Q', 'L', 'S', 'T'],
    ['P', 'Z', 'B', 'G', 'J', 'T'],
    ['D', 'T', 'L', 'J', 'Z', 'B', 'H', 'C'],
    ['G', 'V', 'B', 'J', 'S'],
    ['P', 'S', 'Q'],
    ['B', 'V', 'D', 'F', 'L', 'M', 'P', 'N'],
    ['P', 'S', 'M', 'F', 'B', 'D', 'L', 'R'],
    ['V', 'D', 'T', 'R']
]

# stacks = [
#     ['Z', 'N'],
#     ['M', 'C', 'D'],
#     ['P']
# ]


def get_input(input_line: str):
    split_line = input_line.strip().split(' ')
    stack_amount = split_line[1]
    start_block = split_line[3]
    end_block = split_line[5]
    return int(stack_amount), int(start_block) - 1, int(end_block) - 1


def perform_step_single_crate(command: str):
    stack_amount, start_block, end_block = get_input(command)
    for _ in range(stack_amount):
        shifting_block = stacks[start_block].pop()
        stacks[end_block].append(shifting_block)


def perform_step_full_crate(command: str):
    stack_amount, start_block, end_block = get_input(command)
    queue = []
    for _ in range(stack_amount):
        shifting_block = stacks[start_block].pop()
        queue.append(shifting_block)
    while queue:
        stacks[end_block].append(queue.pop())


def part_1(input_line: str):
    perform_step_single_crate(input_line)
    pass


def part_2(input_line: str):
    perform_step_full_crate(input_line)
    pass


if __name__ == '__main__':
    with open('input.csv', 'r') as file:
        for line in file:
            # part_1(line)
            part_2(line)
    result_string = ''.join([stack[-1] for stack in stacks])
    print(f'Top stack are: {result_string}')
