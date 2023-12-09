
def load_input_as_int_array(file):
    with open(file) as f:
        text = f.readlines()
    return [int(row.strip()) for row in text]

def load_as_string_array(file):
    with open(file) as f:
        text = f.readlines()
    return [row.strip() for row in text]

def read_lines_until_line_break(file):
    with open(file) as f:
        text = f.readlines()
        print(len(text))
        last_num = 0
        arr = []
        for line in text:
            if line != '\n':
                last_num += int(line)
            else :
                arr.append(last_num)
                last_num = 0
        print(len(arr))
        return arr


def string_array_to_int_array(string_nums):
    output = []
    for num in string_nums:
        try:
            number = int(num)
            output.append(number)
        except:
            pass
    return output


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'