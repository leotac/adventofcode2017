with open("day5.txt") as f:
    instructions = [int(l.strip()) for l in f]

l = len(instructions)
pos = 0
jump = 0
steps = 0
while pos < len(instructions) and pos >= 0:
    jump = instructions[pos]
    instructions[pos] += 1
    pos += jump
    steps += 1

print(steps)


with open("day5.txt") as f:
    instructions = [int(l.strip()) for l in f]

l = len(instructions)
pos = 0
jump = 0
steps = 0
while pos < len(instructions) and pos >= 0:
    jump = instructions[pos]
    if jump >= 3:
        instructions[pos] -= 1
    else:   
        instructions[pos] += 1
    pos += jump
    steps += 1

print(steps)
