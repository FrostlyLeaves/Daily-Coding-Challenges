ENDS_HERE = '#'

"""
We simply must change "insert" so it takes an integer and stores this as its final value instead of "True".
"sum" just uses "find" but then adds together all the values that those strings store

It ended up being more complicated than this
"""

def get_value(tip):
    result = 0
    if isinstance(tip, int):
        return tip
    for _, value in tip.items():
        result += get_value(value)
    return result

class PrefixMapSum:
    def __init__(self):
        self._trie={}
    
    def to_string(self):
        print(self._trie)
    
    def insert(self, text, value):
        trie = self._trie
        for char in text:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie[ENDS_HERE] = value

    def find(self, prefix):
        trie = self._trie
        for char in prefix:
            if char in trie:
                trie = trie[char]
            else:
                return None
        return trie
    
    def sum(self, str):
        tip = self.find(str)
        return get_value(tip)


t = PrefixMapSum()
t.insert("dog", 3)
t.insert("dig", 1)
t.insert("mog",2)
t.insert("dug",7)
print(t.sum("d"))

t2 = PrefixMapSum()
t2.insert("columnar", 3)
assert t2.sum("col") == 3
t2.insert("column", 2)
t2.sum("col")
assert t2.sum("col") == 5