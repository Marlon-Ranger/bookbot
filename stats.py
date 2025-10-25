def count_words(text):
    return len(text.split())

def count_characters(text):
    char_dict = {}
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on_num(items):
    return items["num"]

def sort_characters(char_dict):
    char_list = []
    for key,value in char_dict.items():
        char_list.append({"char": key, "num": value})
    char_list.sort(reverse=True, key=sort_on_num)
    return char_list
