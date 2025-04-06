def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    text = text.lower()
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_character_counts(char_counts):
    char_list = [{"char": char, "count": count} for char, count in char_counts.items()]
    char_list.sort(key=lambda x: x["count"], reverse=True)
    return char_list