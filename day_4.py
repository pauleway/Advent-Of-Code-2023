from common_functions import load_as_string_array, string_array_to_int_array


def calculate_card_val(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        return pow(2 ,(num - 1))

def count_winning_numbers(winning_nums, line):
    count = 0
    for num in winning_nums:
        if num in line:
            count += 1
    return count

def part_1(data):
    winning_numbers = []
    card_numbers = []
    total_score = 0
    for line in data:
        numbers = line.split(':')[1].strip()
        winning, card_nums = numbers.split('|')

        string_nums = winning.split(' ')
        w = string_array_to_int_array(string_nums)

        string_nums = card_nums.split(' ')
        c = string_array_to_int_array(string_nums)

        winning_numbers.append(w)
        card_numbers.append(c)

        num_of_winning_numbers = count_winning_numbers(w,c)

        total_score += calculate_card_val(num_of_winning_numbers)
    # for win in winning_numbers:
    #     print(win)
    # for card in card_numbers:
    #     print(card)
    return total_score


if __name__ == '__main__':
    data = load_as_string_array('day_4_data.txt')
    answer = part_1(data)
    print(answer)
    # print(calculate_card_val(1))
    # print(calculate_card_val(2))
    # print(calculate_card_val(3))
    # print(calculate_card_val(4))