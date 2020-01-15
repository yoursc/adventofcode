file_path = "input.txt"


def check_a(line: str):
    if len(line) == 0:
        return False
    vowels_count = 0
    for word in line:
        if word in ['a', 'e', 'i', 'o', 'u']:
            vowels_count += 1
    if vowels_count >= 3:
        return True
    else:
        return False


def check_b(line: str):
    line_l = len(line)
    if line_l == 0:
        return False
    index = 0
    while 1:
        word = line[index]
        word_n = line[index + 1]
        if word == word_n:
            return True
        index += 1
        if index >= line_l - 1:
            return False


def check_c(line: str):
    line_l = len(line)
    if line_l == 0:
        return False
    index = 0
    while 1:
        word = line[index]
        word_n = line[index + 1]
        words = f'{word}{word_n}'
        if words in ["ab", "cd", "pq", "xy"]:
            return False
        index += 1
        if index >= line_l - 1:
            return True


with open(file_path, 'r', encoding='utf8') as file:
    file_str = file.read()
file_list = file_str.split("\n")

nice_count = 0
for line in file_list:
    if check_a(line) and check_b(line) and check_c(line):
        nice_count += 1
print(nice_count)
