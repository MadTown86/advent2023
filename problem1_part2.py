from collections import defaultdict

num = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numbs = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def countNum(line):
    """
    Core function to solve problem 1 part 2 of advent of code 2023.
    :param line: (str)
    :return: sum of all first and last numbers in the line whether written in word or number form.
    """
    location_array = dict()

    # Recursive function to find locations of all word number forms and add to location_array
    def rec_lookup(word: str, line: str, step) -> str:
        if not line:
            return ""
        else:
            if word in line:
                location_array[line.index(word)+step] = numbs[num.index(word)]
                step += len(word)
                return rec_lookup(word, line[line.index(word) + 1:], step)
            else:
                return ""

    for n in num:
        step = 0
        rec_lookup(n, line, step)

    x = 0

    while x < len(line):
        if line[x] in numbs:
            y = x
            while y < len(line) and line[y] in numbs:
                y += 1
            if y == len(line)-1:
                location_array[x] = line[x:].strip()
            else:
                location_array[x] = line[x:y]
            x = y
        else:
            x += 1

    return int(max(location_array.items()[1])) + int(min(location_array.items()[1]))

def main():
    with open('input1.txt', 'r') as f:
        lines = f.readlines()
        for line in range(0, 10, 1):
            print(countNum(lines[line]))

main()