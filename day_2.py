from common_functions import load_as_string_array


def attempt_is_possible(attempts):
    color_max = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    game_attempts = attempts.split(';')
    for attempt in game_attempts:
        for pull in attempt.split(','):
            value, color = pull.strip().split(' ')
            if int(value) > color_max[color]:
                return False
    return True

def part_1(data):
    # Part 1
    total = 0
    for line in data:
        game, attempts = line.split(": ")
        game_num = int(game.split(" ")[1])

        if attempt_is_possible(attempts):
            total += game_num
    print(total)

def part_2(data):
    total = 0
    for line in data:
        game, attempts = line.split(": ")
        # game_num = int(game.split(" ")[1])

        game_attempts = attempts.split(';')
        total += find_power(game_attempts)
    print(f"Total: {total}")

def find_power(game_attempts):
    color_actuals = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for attempt in game_attempts:
        for pull in attempt.split(','):
            value, color = pull.strip().split(' ')
            if int(value) > color_actuals[color]:
                color_actuals[color] = int(value)
    return color_actuals['red'] * color_actuals['green'] * color_actuals['blue']


if __name__ == '__main__':
    data = load_as_string_array('day_2_data.txt')

    # part_1(data)
    part_2(data)



