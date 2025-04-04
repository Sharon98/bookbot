def word_count(content_string):
    count = content_string.split()    
    return len(count)

def unique_char(content_string):
    lower = content_string.lower()
    char_dict = dict()
    for c in lower:
        if c not in char_dict:
            char_dict[c] = 1
        else:
            char_dict[c] += 1
    return char_dict