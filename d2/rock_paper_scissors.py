# read txt file in
path = "/Users/jliuu/Documents/Github/personal/advent-of-code-2022/d2/input.txt"
text_file = open(path, "r")
input_str = text_file.read()
text_file.close()

# input_str = """A Y
# B X
# C Z"""

matches = input_str.split("\n")
matches = [match.split(" ") for match in matches]

score_a = 0
score_b = 0
for match in matches:
    op = match[0]
    me = match[1]

    ms_a = 0
    ms_b = 0

    # if op plays rock
    if op == 'A':
        if me == 'X':
            ms_a += 1 + 3
            ms_b += 0 + 3
        if me == 'Y':
            ms_a += 2 + 6
            ms_b += 3 + 1
        if me == 'Z':
            ms_a += 3 + 0
            ms_b += 6 + 2

    # if op plays paper
    if op == 'B':
        if me == 'X':
            ms_a += 1 + 0
            ms_b += 0 + 1
        if me == 'Y':
            ms_a += 2 + 3
            ms_b += 3 + 2
        if me == 'Z':
            ms_a += 3 + 6
            ms_b += 6 + 3

    # if op plays scissors
    if op == 'C':
        if me == 'X':
            ms_a += 1 + 6
            ms_b += 0 + 2
        if me == 'Y':
            ms_a += 2 + 0
            ms_b += 3 + 3
        if me == 'Z':
            ms_a += 3 + 3
            ms_b += 6 + 1

    score_a += ms_a
    score_b += ms_b

print("if XYZ means what you play: ", score_a)
print("if XYZ means what you win: ", score_b)