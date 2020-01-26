import os


def length_l(line: str):
    lens: int = len(line)
    return lens


def length_s(line: str):
    lens: int = len(line)
    if lens <= 2:
        return 0
    str_in = line[1:lens - 1]
    print(f"str without \"\" is : {str_in}")
    str_out = ""
    index: int = 0
    while 1:
        if index >= lens - 2:
            break
        # 普通字符
        if str_in[index] != "\\":
            str_out += str_in[index]
            index += 1
        # 转义字符-字节码
        elif str_in[index + 1] == "x":
            str_out += str_in[index + 1]
            index += 4
        # 转义字符-普通
        else:
            str_out += str_in[index + 1]
            index += 2
    print(str_out)
    return len(str_out)


with open("input.txt", 'r', encoding='utf8') as file:
    file_str = file.read()
str_list = file_str.split("\n")

num = 0
for line in str_list:
    num += length_l(line) - length_s(line)

print(num)
