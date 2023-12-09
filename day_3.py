from common_functions import load_as_string_array

def collect_ranges(data):
    # Collect ranges
    ranges = []
    first_x = -1
    last_x = -1
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] in "1234567890":
                if first_x == -1:
                    first_x = col
            else:
                if first_x != -1 or col == len(data[0]):
                    last_x = col
                    ranges.append((row, (first_x, last_x)))
                    first_x = -1
                    last_x = -1
        if first_x != -1:
            last_x = len(data[0])
            ranges.append((row, (first_x, last_x)))
            first_x = -1
            last_x = -1
    return ranges

def collect_gears(data):
    gear_locations = []
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] == "*":
                gear_locations.append((row, col))
    return gear_locations

def is_adjacent_to_symbol(row, col_range, data):
    for row_modifier in [-1, 0, 1]:
        for col_modifier in [-1, 0, 1]:
            row_loc = row + row_modifier
            for col in range(col_range[0], col_range[1]):
                col_loc = col + col_modifier
                if 0 <= row_loc < len(data):
                    if 0 <= col_loc < len(data[0]):
                        if data[row_loc][col_loc] not in ".1234567890":
                            return True
    return False

def get_part_num(row, col_range, data):
    output = ""
    for col in range(col_range[0], col_range[1]):
        output += data[row][col]
    return output

def part_1(data):
    # data = [
    #     '.....',
    #     '.999.',
    #     '.....',
    #     '.999$',
    #     '..123']
    ranges = collect_ranges(data)

    print(ranges)
    total = 0
    for row, col_range in ranges:
        is_adj = is_adjacent_to_symbol(row, col_range, data)
        part = get_part_num(row, col_range, data)
        print(f"{part} - row: {row}, col: {col_range}, is_adj: {is_adj}")

        if is_adj:
            total += int(part)
    return total


def part_2(data):
    ranges = collect_ranges(data)
    gear_locs = collect_gears(data)
    total = 0
    for row, col in gear_locs:
        count_of_part_nums = 0
        part_nums = []
        for r in [-1, 0, 1]:
            for c in [-1, 0, 1]:
                row_offset = row + r
                col_offset = col + c
                for row_range, col_range in ranges:
                    if row_offset == row_range:
                        for n in range(col_range[0], col_range[1]):
                            if n == col_offset:
                                # print(n)
                                # print(f"\t\toffsets: r:{row_offset}, c:{col_offset}")
                                # print(f"\t\tpartNumRow: {row_range}, partNumCol: ", end="")
                                # for column in range(int(col_range[0]), int(col_range[-1])):
                                #     print(column, end=",")
                                # print(f"\t\t\t\t\t\t{col_range}")
                                part_num = get_part_num(row_offset, col_range, data)
                                print(f" PartNum: {part_num}")
                                if part_num not in part_nums:
                                    count_of_part_nums += 1
                                    part_nums.append(part_num)
        print(part_nums)
        if count_of_part_nums == 2:
            total += int(part_nums[0]) * int(part_nums[1])
    return total

if __name__ == '__main__':
    data = load_as_string_array('day_3_data.txt')
    # answer = part_1(data)
    # print("-----------")
    # print(answer)
    answer = part_2(data)
    print(answer)