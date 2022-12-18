# read txt file in
path = "/Users/jliuu/Documents/Github/personal/advent-of-code-2022/d1/input.txt"
text_file = open(path, "r")
input_str = text_file.read()
text_file.close()

# parse txt file
elfs = input_str.split('\n\n')
elf_calories = [0] * len(elfs)

# process txt file
for i in range(len(elfs)):
    elfs[i] = elfs[i].split('\n')
    elfs[i] = [int(x) for x in elfs[i]]
    elf_calories[i] = sum(elfs[i])

# part 1 - max value
print(max(elf_calories))

# part 2 -
elf_calories.sort()
print(sum(elf_calories[-3:]))