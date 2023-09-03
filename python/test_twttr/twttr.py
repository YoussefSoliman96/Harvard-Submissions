def main():
    word =  input("Input: ").lower()
    shorten(word)



def shorten(word):
    for c in word:
        if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
            v = c.replace("c", "")
            print(v, end="")
        else:
            print(c, end="")
    return word



if __name__ == "__main__":
    main()