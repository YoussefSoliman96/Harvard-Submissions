from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"




if __name__ == "__main__":
    main()