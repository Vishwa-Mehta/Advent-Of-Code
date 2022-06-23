def find_position(steps: [[int]]) -> int:
    h_pos = 0
    v_pos = 0
    for step in steps:
        if step[0] == "forward":
            h_pos += int(step[1])
        elif step[0] == "down":
            v_pos += int(step[1])
        else:
            v_pos -= int(step[1])
    return h_pos * v_pos
steps = input("enter the steps: ").split(" ")
step = []
for i in steps:
    step.append(i.split(","))
position_product = find_position(step)
print(position_product)
