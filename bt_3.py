input_str = input("nhap mot chuoi bat ki tu ban phim: ")

print(f"ki tu lon nhat torng chuoi la : {max(input_str)}")

min_character = input_str[0]
for item in input_str:
    if min_character < item:
        min_character = item
print(f"ki tu nho nhat trong chuoi la : {min_character}")

#item lay ki tu
#i range(len(s)) cho chi so torng ham