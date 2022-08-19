numbers = [55, 4, 92, 1, 104, 64, 73, 99, 20]

max_value = None

for num in numbers:
    if (max_value is None or num > max_value):
        max_value = num

print('Maximum value:', max_value)


print("      ")
numbers = [55, 4, 92, 1, 104, 64, 73, 99, 20]

max_value = None
max_idx = None

for idx, num in enumerate(numbers):
    if (max_value is None or num > max_value):
        max_value = num
        max_idx = idx

print('Maximum value:', max_value, "At index: ", max_idx)
