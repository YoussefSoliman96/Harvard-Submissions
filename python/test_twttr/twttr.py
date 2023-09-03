def main():
    word =  input("Input: ").lower()
    new_message = shorten(word)
    print("Output: " + new_message)



def shorten(word):
    new_word = ""
    for c in word:
        if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
            v = c.replace(c, "")
            new_word += v
        else:
            new_word += c
    return new_word

if __name__ == "__main__":
    main()