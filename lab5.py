if __name__ == "__main__":
    user_input = input("Enter a string: ").strip().lower()
    split_input = user_input.split(" ")
    strip_input = []
    for i in range(len(split_input)):
        strip_input.append(split_input[i].strip())
    joined_input = "".join(strip_input)
    isOffset = False
    for k in range(1, len(joined_input)):
        settings = (joined_input[k:]) + (joined_input[:k])
        if (settings == joined_input) and (len(settings) % len(joined_input)) < len(joined_input):
            print(f"{joined_input} is a rotation with offset: {k}")
            isOffset = True
        while (not isOffset) and (k >= ((1/2) * len(joined_input))):
            print("There are no rotations of the string")
            isOffset = True

