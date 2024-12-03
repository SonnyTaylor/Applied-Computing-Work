from collections import Counter


def main():
    with open("novel.txt", "r", encoding="utf-8") as file:
        text = file.read()
    words = text.split()
    capital_words = [word for word in words if word[0].isupper()]
    counter = Counter(capital_words)
    top_three = counter.most_common(3)
    for word, count in top_three:
        print(f"{count} {word}")


if __name__ == "__main__":
    main()
