def count_words(content):
    counter = 0

    for word in content.split():
        counter += 1

    return counter 

def count_charactes(content):
    characters = {}

    for character in content.lower():
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1

    return characters


def print_report(words, characters):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document\n")

    for character in characters:
        if character.isalpha():
            print(f"The '{character}' character was found {characters[character]} times")  

    print("--- End report ---")


def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()

        words = count_words(file_contents)
        characters = count_charactes(file_contents)

        print_report(words, characters)

main()