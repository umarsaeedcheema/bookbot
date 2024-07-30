with open('./books/frankenstein.txt') as f:
    file_contents = f.read()


def count_words(text: str) -> int:
    words = text.split()
    return len(words)


def count_characters(text: str) -> dict:
    characters = {}
    text = text.lower()
    for i in text:
        if i not in characters:
            characters[i] = 0
        characters[i] += 1
    return characters


def main():
    print(count_words(file_contents))
    print(count_characters(file_contents))


main()
