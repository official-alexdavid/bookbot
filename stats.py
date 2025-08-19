def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    text = text.lower()
    chars = {}
    for c in text:
        if c not in chars:
            chars[c] = text.count(c)
    return chars

def sort_on(items):
    sorted = []
    for key in items:
        if key.isalpha():
            item = {'name': key, 'count': items[key]}
            sorted.append(item)
    sorted.sort(key=lambda x: x['count'], reverse=True)
    return sorted