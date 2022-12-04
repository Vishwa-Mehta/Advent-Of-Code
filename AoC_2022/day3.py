import sys

def get_items() -> [[str]]:
    item = []
    for _ in sys.stdin:
        item.append(_.strip())
    return item

def get_common_letter(a:str, b:str) -> str:
    for i in a:
        if i in b:
            return i

def get_common_item(item:[[str]]) -> [str]:
    common_item = []
    for i in item:
        common_item.append(get_common_letter(i[:len(i)//2], i[len(i)//2:]))
    return common_item

def get_sum_priorities(common_items:[str]) -> int:
    priority = {}
    a = 'a'
    A = 'A'
    priorities = []
    for i in range(1,27):
        priority[a] = i
        priority[A] = i + 26
        a = chr(ord(a) + 1)
        A = chr(ord(A) + 1)

    for i in common_items:
        priorities.append(priority[i])

    return sum(priorities)

# part 2
def get_common_letters(a:str, b:str) -> [str]:
    letters = ""
    for i in a:
        if i in b:
            letters += i
    return letters

def get_badge(item:[[str]]) -> [str]:
    groups = []
    common_items = []
    for i in range(0, len(item), 3):
        groups.append(item[i:i+3])
    for _ in groups:
        x, y, z = get_common_letters(_[1], _[2]), get_common_letters(_[1], _[0]), get_common_letters(_[0], _[2])
        common_items.append(get_common_letter(x, y))
    return common_items

items = get_items()
# part 1
print(get_sum_priorities(get_common_item(items)))
# part 2
print(get_sum_priorities(get_badge(items)))
