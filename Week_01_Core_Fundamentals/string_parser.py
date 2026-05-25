"""
TASK: 05 String Parser

# String Parser
Write a parser that:
- Accepts a sentence from the user.
- Splits it into words manually (not using split()).
- Outputs number of words + list of words.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def count_words(sentence):
    words = []
    current = ""
    for char in sentence:
        if char == " ":
            if current != "":
                words.append(current)
                current = ""
        else:
            current += char
    if current != "":
        words.append(current)
    return len(words)


def is_palindrome(sentence):
    cleaned = "".join(ch.lower() for ch in sentence if ch.isalnum())
    return cleaned == cleaned[::-1]


def main():
    sentence = input("Enter a sentence: ")
    print(count_words(sentence))
    print(is_palindrome(sentence))


if __name__ == "__main__":
    main()
