from common_functions import load_as_string_array

if __name__ == '__main__':
    arr = load_as_string_array('day_1_data.txt')
    numbers = {
               'one': 1,
               'two': 2,
               'three': 3,
               'four': 4,
               'five': 5,
               'six': 6,
               'seven': 7,
               'eight': 8,
               'nine': 9
               # 'ten': 10,
               # 'eleven': 11,
               # 'twelve': 12,
               # 'thirteen': 13,
               # 'fourteen': 14,
               # 'fifteen': 15,
               # 'sixteen': 16,
               # 'seventeen': 17,
               # 'eighteen': 18,
               # 'nineteen': 19,
               # 'twenty': 20
               }


    num_array = []
    for line in arr:
        line_arr = []

        for i in range(len(line)):
            char = line[i]
            if char in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                line_arr.append(char)
            forward_line = line[i:]
            for word in numbers.keys():
                index = forward_line.find(word)
                if index == 0:
                    line_arr.append(numbers[word])

        num_array.append((int(line_arr[0]), int(line_arr[-1])))
    answer = 0
    # print(num_array)
    for first, last in num_array:
        print(f"{first}, {last}")
        if last == -1:
            last = ""
        num = int(f"{first}{last}")
        answer += num
    print("________________")
    print(answer)
