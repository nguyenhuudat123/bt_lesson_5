input_str = input("nhap mot chuo bat ki: ")
char = input('nhap vao mot ki tu bat ki: ')
for i in range(len(input_str)):
    if input_str[i] == char:
        print(i, end='; ')

