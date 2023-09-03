def main():
    word =  input("Input: ")
    shorten(word)


def shorten(word):
    for c in word:
        print(c)
    return word



if __name__ == "__main__":
    main()