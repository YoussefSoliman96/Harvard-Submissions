def main():

    text = str(input("Text: "))
    letters = get_letters()
    words = get_words()
    sentences
    L = float(letters) / float(words) * 100
    S = float(words) / float(sentences) * 100
    index = 0.0588 * L - 0.296 * S - 15.8






def get_words(text):
    count = 0
    for c in text:
        if c == " ":
            count += 1
    return count

def get_letters()


if __name__ == "__main__":
    main()