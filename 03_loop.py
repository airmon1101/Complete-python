names = ["Hytes", "Meera", "Sam", "Sunny"]
bills = [50,95,56,84]
for name, amount in zip(names, bills):
    print(f"{name} paid ${amount} Dollar")
