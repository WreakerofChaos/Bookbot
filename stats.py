def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    chars = {}
    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_output(chars):
    character_list = []
    for char, count in chars.items():
        character_list.append({"char":char, "count": count})

    def sort_on(dict_item):
        return dict_item["count"]
        
    character_list.sort(reverse=True, key=sort_on)

    return character_list