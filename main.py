def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read() 
    
    words = file_contents.split()
    num_words = len(words)

    
    lower_file_contents = file_contents.lower()
    
    character_count = dict()
    
    for char in lower_file_contents:
        if character_count.get(char) is not None:
            character_count[char] += 1
        else:
            character_count[char] = 1
    
    sorted_character_count = dict(sorted(character_count.items(), key=lambda item: item[1], reverse=True))
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document.")
    print()
    for key in sorted_character_count.keys():
        value =sorted_character_count[key]
        if 'a' <= key <= 'z':
            print(f"The '{key}' character was found {value} times")


main()





