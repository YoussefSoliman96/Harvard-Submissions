def main():
    greeting = input("Input: ")
    greeting = value(greeting)
    print(f"Output: ${greeting}")


def value(greeting):
    words = greeting.lower().strip()
    words = words.split(" ")
    first = words[0].replace(",", "")
    if first == "hello":
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()