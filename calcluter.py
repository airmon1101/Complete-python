num_1 = int(input('Enter 1st number: '))
num_2 = int(input('Enter 2nd number: '))

choice = input("enter your choice '+,-,/,*' = ")


if choice == '+':
    print(f"Addition: {num_1 + num_2}")
elif choice == '-':
    print(f"Subtraction: {num_1 - num_2}")
elif choice == '/':
    print(f"Devision: {num_1 / num_2}")
elif choice == '*':
    print(f"Multipliction: {num_1 * num_2}")
else:
    print("Envlaid choise")