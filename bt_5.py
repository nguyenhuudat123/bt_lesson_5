input_str = input("nhap mot chuo bat ki: ")
for item in input_str:
    if item.isnumeric() == 1:
        print(item, end=', ')
