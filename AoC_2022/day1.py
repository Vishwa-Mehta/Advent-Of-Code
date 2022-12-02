import sys

line = ""
for _ in sys.stdin:
    line += _.strip()
    line += ","

lines = line.split(',,')
elves = []
max_calories = 0
top_elves = []
for _ in lines:
    _ = _.strip(',')
    l = _.split(',')
    elf = [int(calories) for calories in l]
    if sum(elf) > max_calories:
        max_calories = sum(elf)
        top_elves.append(max_calories)

print(sum(top_elves[-3:]))
print(max_calories)
