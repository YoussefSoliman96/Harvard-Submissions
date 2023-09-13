def main():
    word =  input("Input: ")
    new_message = shorten(word)
    print("Output: " + new_message)


def shorten(word):
    new_word = ""
    for c in word:
        y = c.lower()
        # If current character is a vowel, remove it
        if y == "a" or y == "e" or y == "i" or y == "o" or y == "u":
            v = c.replace(c, "")
            new_word += v
        else:
            new_word += c
    return new_word

if __name__ == "__main__":
    main()