str = input("Input A String")
_char = input("Count This Character")
chars = list(str)
chars = sorted(str)

count = 0

for letter in chars:
    if _char == letter:
        count +=1

print(f"COUNT for {_char} : {count}")

