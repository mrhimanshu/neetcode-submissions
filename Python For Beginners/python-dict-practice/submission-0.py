from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    a = {}
    for w in word:
        if w not in a:
            a[w]=1
        else:
            a[w] += 1
    return a
        




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
