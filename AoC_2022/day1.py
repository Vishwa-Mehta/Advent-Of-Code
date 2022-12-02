import sys

line = ""
for _ in sys.stdin:
    line += _.strip()
    line += ","

lines = line.split(',,')
elves = []
max_calories = 0
top_elves = [] #part 2
for _ in lines:
    _ = _.strip(',')
    l = _.split(',')
    elf = [int(calories) for calories in l]
    if sum(elf) > max_calories:
        max_calories = sum(elf) # part 1
        top_elves.append(max_calories) # part 2

#part 1
print(max_calories)
#part 2
print(sum(top_elves[-3:]))
