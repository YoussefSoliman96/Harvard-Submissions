def main():
    word =  input("Input: ").lower()
    new_word = shorten(word)
    print(new_word)


def shorten(word):
    for c in word:
        if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
            word = c.replace("c", "")
    return word



if __name__ == "__main__":
    main()