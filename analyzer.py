def count_words(text):
    return len(text.split())


def count_characters(text):
    return len(text)


def count_vowels(text):
    return sum(1 for char in text.lower() if char in 'aeiou')


def reverse_text(text):
    return text[::-1]
