if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        try:
            input_string = input().split(" ")
        except ValueError:
            pass
        command = input_string[0]
        if len(input_string) == 2:
            attribute = int(input_string[1])
        if len(input_string) == 3:
            attribute_2 = int(input_string[2])

        if command.lower() == "append":
            arr.append(attribute)
        elif command.lower() == "remove":
            arr.remove(attribute)
        elif command.lower() == "insert":
            arr.insert(attribute, attribute_2)
        elif command.lower() == "pop":
            arr.pop()
        elif command.lower() == "sort":
            arr.sort()
        elif command.lower() == "reverse":
            arr.reverse()
        elif command.lower() == "print":
            print(arr)


