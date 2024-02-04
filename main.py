def main():
    import os
    #os.chdir("/Users/nelsonschaub/codingz/github.com/mtrptre/bookbot")

    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_count = get_words_count(text)
    letters_count = get_letters_count(text)

    #print (text)
    print(words_count)
    print(len(text))
    print(letters_count)
    print(f"--- Begin report of {book_path} ---")
    make_report(text)


    



def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_words_count(text):
    text_split = text.split()
    words_count = len(text_split)
    return words_count

def get_letters_count(text):
    import string
    alphabet = list(string.ascii_lowercase)

    letters_count = {}
    for letter in alphabet:
        num_letter = text.lower().count(letter)
        letters_count[letter] = num_letter
    return letters_count

def make_report(text):
    print(f"{get_words_count(text)} words found in the document")
    dic_letters = get_letters_count(text)
    
    for letter in dic_letters:
        print(f"the '{letter}' was found {dic_letters[letter]} times ")


###########
    def get_chars_dict(text):
        chars = {}
        for c in text:
            lowered = c.lower()
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
        return chars
            
    


main()

