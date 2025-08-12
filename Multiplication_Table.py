def multiplication_table(number):
    table = []  # empty list to store results
    for i in range(1, 11):
        result = number * i
        table.append(f"{number} x {i} = {result}")
    return table

# print(multiplication_table(5))

for line in multiplication_table(5):
    print(line)
