import sys

def get_input() -> [[str]]:
    i = []
    for _ in sys.stdin:
        _ = _.strip('\n')
        i.append(_)
    i1 = i[:i.index('')]
    i2 = i[i.index('')+1:]
    return [i1, i2]

def get_stack(i:[str]) -> [[str]]:
    s = []
    stacks = []
    no_of_stacks = int(i[-1][-2])
    for j in i[:-1]:
        for k in range(1, len(j), 4):
            s.append(j[k])
    for j in range(no_of_stacks):
        x = []
        for k in range(j, len(s), no_of_stacks):
            if s[k] != ' ':
                x.append(s[k])
        stacks.append(x)
    return stacks

def get_moves(i:[str]) -> [[int]]:
    moves = []
    for j in i:
        numbers = []
        j = j.split(' ')
        for k in j:
            if k.isnumeric():
                numbers.append(int(k))
        moves.append(numbers)
    return moves

# part 1
def shift_crates(stacks:[[str]], moves:[[int]]) -> [[str]]:
    for move in moves:
        for x in range(move[0]):
            stacks[move[2]-1].insert(0, stacks[move[1]-1][0])
            stacks[move[1]-1].pop(0)
    return stacks

# part 2
def shift_crates_in_order(stacks:[[str]], moves:[[int]]) -> [[str]]:
    for move in moves:
        for x in range(move[0]-1, -1, -1):
            stacks[move[2]-1].insert(0, stacks[move[1]-1][x])
            stacks[move[1]-1].pop(x)
    return stacks

def find_top_crates(stacks:[[str]]) -> [str]:
    crates = []
    for stack in stacks:
        crates.append(stack[0])
    return crates

inp = get_input()

# part 1
stacks = get_stack(inp[0])
moves = get_moves(inp[1])
shifted_stack = shift_crates(stacks, moves)
print(find_top_crates(shifted_stack))

# part 2
stacks = get_stack(inp[0])
moves = get_moves(inp[1])
new_shift = shift_crates_in_order(stacks, moves)
print(find_top_crates(new_shift))
