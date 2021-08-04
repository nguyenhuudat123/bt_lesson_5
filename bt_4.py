input_str = input("nhap mot chuo bat ki: ")
new_str = ""
for item in input_str:
    if 65 <= ord(item) <= 90:
        new_str += chr(ord(item) + 32)
    elif 97 <= ord(item) <= 122:
        new_str += chr(ord(item) - 32)
    else:
        new_str += item
print(f'chuoi moi la : {new_str}')

print(f"chuoi sau khi dao nguoc la: {input_str.swapcase()}")