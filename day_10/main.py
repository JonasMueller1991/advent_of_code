from collections import deque
from itertools import cycle

command_register = deque([])
register_value = 1


def fill_register(line: str):
    global command_register
    if line.strip() == 'noop':
        command_register.append(None)
    else:
        _, add_value = line.strip().split(' ')
        command_register.append(None)
        command_register.append(int(add_value))


def part_1():
    global register_value
    register_counter = 0
    signal_strengths = []
    while command_register:
        register_counter += 1
        if (register_counter - 20) % 40 == 0:
            # print(f'Current register counter: {register_counter} : {register_value}')
            signal_strengths.append(register_counter * register_value)

        instruction = command_register.popleft()
        if instruction:
            register_value += instruction
    print(f'Sum of all signal strengths: {sum(signal_strengths)}')


def get_pixel(cycle, current_register_value):
    if abs(cycle - current_register_value) > 1:
        return ' '
    else:
        return '#'


def part_2():
    global register_value
    NUM_PIXELS = 240
    frame = []
    for cycle in range(NUM_PIXELS):
        if cycle % 40 == 0:
            frame.append('\n')
        frame_index = cycle % 40
        frame.append(get_pixel(frame_index, register_value))
        instruction = command_register.popleft()
        if instruction:
            register_value += instruction

    print(''.join(frame))


if __name__ == '__main__':
    with open('input.csv', 'r') as file:
        for line in file:
            fill_register(line)
    part_2()
