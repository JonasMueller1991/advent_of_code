DRAW_VALUE = 3
LOSE_VALUE = 0
WIN_VALUE = 6


class Rock:
    @classmethod
    def against(cls, opponent):
        if isinstance(opponent, Scissor):
            return WIN_VALUE
        if isinstance(opponent, Rock):
            return DRAW_VALUE
        if isinstance(opponent, Paper):
            return LOSE_VALUE

    additional_score = 1


class Paper:
    @classmethod
    def against(cls, opponent):
        if isinstance(opponent, Scissor):
            return LOSE_VALUE
        if isinstance(opponent, Rock):
            return WIN_VALUE
        if isinstance(opponent, Paper):
            return DRAW_VALUE

    additional_score = 2


class Scissor:
    @classmethod
    def against(cls, opponent):
        if isinstance(opponent, Scissor):
            return DRAW_VALUE
        if isinstance(opponent, Rock):
            return LOSE_VALUE
        if isinstance(opponent, Paper):
            return WIN_VALUE

    additional_score = 3


def get_instance(input: str):
    match input:
        case "A" | "X":
            return Rock()
        case "B" | "Y":
            return Paper()
        case "C" | "Z":
            return Scissor()
        case _:
            raise ValueError("No valid input.")


def get_strategy_pair(elve_pick: str, ending: str):
    match ending:
        case "X":  # Loosing
            match elve_pick:
                case "A":
                    return get_instance("A"), get_instance("C")
                case "B":
                    return get_instance("B"), get_instance("A")
                case "C":
                    return get_instance("C"), get_instance("B")
        case "Y":  # Drawing
            match elve_pick:
                case "A":
                    return get_instance("A"), get_instance("A")
                case "B":
                    return get_instance("B"), get_instance("B")
                case "C":
                    return get_instance("C"), get_instance("C")
        case "Z":  # Winning
            match elve_pick:
                case "A":
                    return get_instance("A"), get_instance("B")
                case "B":
                    return get_instance("B"), get_instance("C")
                case "C":
                    return get_instance("C"), get_instance("A")


def get_score_part1(elve_pick_label: str, my_pick_label: str):
    elve_pick = get_instance(elve_pick_label)
    my_pick = get_instance(my_pick_label)
    return my_pick.against(elve_pick) + my_pick.additional_score


def get_score_part2(elve_pick_label: str, ending_label: str):
    elve_pick, my_pick = get_strategy_pair(elve_pick_label, ending_label)
    return my_pick.against(elve_pick) + my_pick.additional_score


def part_1():
    total_score = 0
    with open('guide.csv') as file:
        for line in file:
            elve_pick, my_pick = line.split()
            total_score += get_score_part1(elve_pick, my_pick)
    print(f'total score: {total_score}')


def part_2():
    total_score = 0
    with open('guide.csv') as file:
        for line in file:
            elve_pick, ending_label = line.split()
            total_score += get_score_part2(elve_pick_label=elve_pick, ending_label=ending_label)
    print(f'total score: {total_score}')


if __name__ == '__main__':
    # part_1()
    part_2()
