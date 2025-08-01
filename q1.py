
# ask for the range
start = int(input("Enter start: "))
stop  = int(input("Enter stop: "))

# ask which number to skip
skip  = int(input("Enter a number you want to skip: "))

# validate inputs
if start >= stop:
    print("Invalid entry: start must be less than stop.")
else:
    # check whether skip is actually in [start, stop]
    if not (start <= skip < stop):
        print(f"Note: skip value {skip} is outside the range [{start}, {stop}]; nothing will be skipped.")

    # iterate from start up to stop-1
    for num in range(start, stop):
        if num == skip:
            # only hits if skip is in-range
            continue
        print(num)
