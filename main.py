def main():
    with open("books/frankenstein.txt") as book:
        file_contents = book.read()
        wordcount(file_contents)
        num_char_report(character_count(file_contents))

def wordcount(string):
    words = string.split()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document")

def character_count(string):
    chars = {}
    for i in string.lower():
        if i in chars:
            chars[i] += 1
        else:
            chars[i] = 1
    return chars
def sort_on(dict):
    return dict["num"]

def num_char_report(dictionary):
    dictlist = []
    for i in dictionary:
        if i.isalpha():
            new_dict = {"char": i, "num": dictionary[i]}
            dictlist.append(new_dict)
    dictlist.sort(reverse=True,key=sort_on)
    for i in dictlist:
        print(f"The '{i["char"]}' character was found {i["num"]} times")
    print("--- End report ---")




if __name__ == "__main__":
    main()