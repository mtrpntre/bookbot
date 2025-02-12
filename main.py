def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()
    return text

def word_count(text):
    return len(text.split())

frankenstein = main()

word_in_frankenstein = word_count(frankenstein)

print(word_in_frankenstein)



