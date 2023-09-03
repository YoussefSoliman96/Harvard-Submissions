def main():
    word =  input("Input: ").lower()
    new_word = shorten(word)
    print("Output: " + new_word)



def shorten(word):
    for c in word:
        if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
            return c.replace("c", "")
        else:
            return c

if __name__ == "__main__":
    main()