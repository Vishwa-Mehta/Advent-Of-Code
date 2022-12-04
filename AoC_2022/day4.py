import sys

def get_sections() -> [[str]]:
    section = []
    for _ in sys.stdin:
        _ = _.strip()
        section.append(_.split(','))
    return section

def section_simplified(sections:[[str]]) -> [[{int}]]:
    simplified = []
    for i in sections:
        x = i[0].split('-')
        x = [int(j) for j in x]
        y = i[1].split('-')
        y = [int(j) for j in y]
        simplified.append([set([sec for sec in range(x[0], x[1]+1)]), set([sec for sec in range(y[0], y[1]+1)])])
    return simplified

# part 1
def find_fully_contianed_pairs(sections:[[{int}]]) -> int:
    fully_contained = 0
    for i in sections:
        union = i[0] | i[1]
        if union == i[1] or union == i[0]:
            fully_contained += 1
    return fully_contained

# part 2
def find_partially_contained_pairs(sections:[[{int}]]) -> int:
    partially_contained = 0
    for i in sections:
        intersection = i[0] & i[1]
        if intersection:
            partially_contained += 1
    return partially_contained

sections = get_sections()
simplified = section_simplified(sections)
#part 1
print(find_fully_contianed_pairs(simplified))
#part 2
print(find_partially_contained_pairs(simplified))
