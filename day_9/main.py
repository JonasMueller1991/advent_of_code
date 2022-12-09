from dataclasses import dataclass
from typing import Set


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


def d(head: Position, tail: Position):
    return (head.x - tail.x) ** 2 + (head.y - tail.y) ** 2


def move_tail(head: Position, tail: Position):
    if d(head, tail) > 2:
        if head.x > tail.x:
            move(tail, 'R')
        if head.x < tail.x:
            move(tail, 'L')
        if head.y > tail.y:
            move(tail, 'U')
        if head.y < tail.y:
            move(tail, 'D')
        # print(f'Current Tail position: ({tail.x}, {tail.y})')


def safe_tail_position(tail: Position):
    global visited_tail_position
    if not tail in visited_tail_position:
        visited_tail_position.append(Position(tail.x, tail.y))


visited_tail_position = [Position(0, 0)]


def perform_command(line: str, head: Position, tail: Position):
    direction, cmd_count = line.strip().split(' ')
    for _ in range(int(cmd_count)):
        move(head, direction)
        move_tail(head, tail)
        safe_tail_position(tail)


if __name__ == '__main__':
    head = Position(0, 0)
    tail = Position(0, 0)
    with open('input.csv', 'r') as file:
        for line in file:
            perform_command(line, head, tail)

    print(f'Last head position: ({head.x}, {head.y})')
    print(f'Last tail position: ({tail.x}, {tail.y})')
    print(f'Visited tail positions: {visited_tail_position}')
    print(f'Count tail positions: {len(visited_tail_position)}')
