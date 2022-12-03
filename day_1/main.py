def part_1():
    maximal_calories = 0
    for current_calories in get_current_calories():
        if current_calories > maximal_calories:
            maximal_calories = current_calories
    print(f'solution_part1 : {maximal_calories}')


def part_2():
    top_three = [0, 0, 0]
    for current_calories in get_current_calories():
        update_top_three(current_calories, top_three)

    print(f'Current top three : {top_three}\n'
          f'Sum of top three: {sum(top_three)}')


def get_current_calories():
    current_calories = 0
    for line in open('calories.csv', "r"):
        if line.strip():
            current_calories += int(line)
        else:
            yield current_calories
            current_calories = 0


def update_top_three(current_calories, top_three):
    if current_calories > top_three[-1]:
        top_three.pop()
        top_three.append(current_calories)
        top_three.sort(reverse=True)


if __name__ == '__main__':
    part_1()
    part_2()

