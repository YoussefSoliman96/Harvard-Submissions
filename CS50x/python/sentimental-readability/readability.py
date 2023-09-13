def main():

    text = str(input("Text: "))
    letters = get_letters(text)
    words = get_words(text)
    sentences = get_sentences(text)
    L = float(letters) / float(words) * 100
    S = float(words) / float(sentences) * 100
    index = 0.0588 * L - 0.296 * S - 15.8
    print(index)
    get_grade(index)




def get_letters(text):
    count = 0
    for c in text:
        if c.isalpha():
            count += 1
    return count

def get_words(text):
    count = 0
    for c in text:
        if c == " ":
            count += 1
    return count

def get_sentences(text):
    count = 0
    for c in text:
        if c == "," or c == "." or c == "?":
            count += 1
    return count

def get_grade(index):
    if index < 1:
        print("Before Grade 1")
    elif index > 16:
        print("Grade 16+")
    else:
        print(f"Grade: {index}")


if __name__ == "__main__":
    main()