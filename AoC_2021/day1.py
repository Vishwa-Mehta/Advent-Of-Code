def number_of_measurements_larger_than_previous(depths: [int]) -> int:
    i = 0
    count = 0
    while (i < len(depths) - 1):
        if depths[i] < depths[i+1]:
            count += 1
        i += 1
    return count

#test_depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
test_depths = input("enter the depths: ").split(" ")
result = number_of_measurements_larger_than_previous(test_depths)
print(result)
