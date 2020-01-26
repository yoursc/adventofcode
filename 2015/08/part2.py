def count(line: str):
    num = 0
    for i in line:
        if i in ("\\","\""):
            num += 1
    return num


with open("input.txt", 'r', encoding='utf8') as file:
    file_str = file.read()
str_list = file_str.split("\n")

num = 0
for line in str_list:
    num += count(line) + 2

print(num)
