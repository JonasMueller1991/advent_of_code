from dataclasses import dataclass
from typing import List


@dataclass(eq=True)
class Position:
    x: float
    y: float


def move(position: Position, direction: str):
    match direction:
        case 'R':
            position.x += 1
        case 'L':
            position.x -= 1
        case 'U':
            position.y += 1
        case 'D':
            position.y -= 1
        case _:
            raise ValueError("Invalid Input")


def distance(head: Position, tail: Position):
    return (head.x - tail.x) ** 2 + (head.y - tail.y) ** 2


def move_tail(head: Position, tail: Position):
    if distance(head, tail) > 2:
        if head.x > tail.x:
            move(tail, 'R')
        if head.x < tail.x:
            move(tail, 'L')
        if head.y > tail.y:
            move(tail, 'U')
        if head.y < tail.y:
            move(tail, 'D')


visited_tail_positions = [Position(0, 0)]


def save_tail_position(tail: Position):
    global visited_tail_positions
    if not tail in visited_tail_positions:
        visited_tail_positions.append(Position(tail.x, tail.y))


def perform_command(line: str, head: Position, tail: Position):
    direction, cmd_count = line.strip().split(' ')
    for _ in range(int(cmd_count)):
        move(head, direction)
        move_tail(head, tail)
        save_tail_position(tail)


def perform_rope_command(line: str, rope: List[Position]):
    direction, cmd_count = line.strip().split(' ')
    for _ in range(int(cmd_count)):
        move(rope[0], direction)
        for rope_id in range(9):
            move_tail(rope[rope_id], rope[rope_id + 1])
        save_tail_position(rope[-1])


def part_1():
    head = Position(0, 0)
    tail = Position(0, 0)
    with open('input.csv', 'r') as file:
        for line in file:
            perform_command(line, head, tail)
    print(f'Last head position: ({head.x}, {head.y})')
    print(f'Last tail position: ({tail.x}, {tail.y})')
    print(f'Visited tail positions: {visited_tail_positions}')
    print(f'Count tail positions: {len(visited_tail_positions)}')


def part_2():
    rope = [Position(0, 0) for _ in range(10)]
    with open('input.csv', 'r') as file:
        for line in file:
            perform_rope_command(line, rope)
    print(f'End of rope saved spaces: {len(visited_tail_positions)}')


if __name__ == '__main__':
    # part_1()
    part_2()
