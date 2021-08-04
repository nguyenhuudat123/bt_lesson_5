input_str = input("nhap mot chuoi bat ki: ")
if len(input_str) < 2:
    print("empty string: "" ")
else:
    new_str = input_str[0] + input_str[1] + input_str[-2] + input_str[-1]
    print(f"new string: {new_str}")