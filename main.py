def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()
    return text

def get_text(text_way):
    with open(text_way) as f:
        text = f.read()
    return text

def word_count(text_way):
    text = get_text(text_way)
    return len(text.split())

def character_count(text):
    lower_text = text.lower()
    list_of_characters = list(lower_text)
    character_dict = {}
    for character in list_of_characters:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

def write_report(text_way):
        text = get_text(text_way)
        wordscount = word_count(text_way)
        character_dict = character_count(text)
        print(f"The report has been written to {text_way}")
        print(f"The text contains {wordscount} words")
        for character in character_dict:
            if character.isalpha():
                print(f"The '{character}' character was found {character_dict[character]} times")
        
        print("---End of report---")



write_report("books/frankenstein.txt")





