def main():

    text = str(input("Text: "))
    letters = get_letters()
    words = get_words()
    L = float(letters) / float(words) * 100
    S = float(words) / float(sentences) * 100
    index = 0.0588 * L - 0.296 * S - 15.8











if __name__ == "__main__":
    main()