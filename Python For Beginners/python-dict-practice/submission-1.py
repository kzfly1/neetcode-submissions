from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    count = {}
    for ch in word:
        count[ch] = count.get(ch, 0) + 1
    return count

    '''
    count = {}
    for ch in word:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
    return count
    '''
        





# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
