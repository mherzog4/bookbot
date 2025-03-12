
def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def get_num_characters(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]

def get_sorted_chars(num_chars_dict):
    sorted_list = []
    for char in num_chars_dict:
        sorted_list.append({"char": char, "num": num_chars_dict[char]})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list