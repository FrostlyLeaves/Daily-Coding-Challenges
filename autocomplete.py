from tries import Trie

"""
.find basically already does this for us. What we have to do is stick the original letters on the
    front of the strings and format the rest of the strings. For example, if we have the quary
    string 'd' and the set ['dog','mog','dig','dug'], .find returns
    {'o': {'g': {'#': True}}, 'i': {'g': {'#': True}}, 'u': {'g': {'#': True}}}. We simply have to
    stick 'd' at the beginning of each string and concatinate them such that 'o': {'g': {'#': True}}
    becomes "dog" and so forth.
"""

def get_word(tip, prefix):
    result = prefix
    while tip != True:
        char = next(iter(tip))
        if (char != "#"):
            result += char
        tip = tip[char]
    return result

def autocomplete(prefix, strings):
    t = Trie()
    result = []
    for s in strings:
        t.insert(s)
    
    tip = t.find(prefix)
    for key, value in tip.items():
        result.append(get_word(value, prefix + key))

    return result
    
print(autocomplete("d", ["dog", "mog", "dig", "dug"]))
print(autocomplete("de", ["dog", "deer", "deal"]))

#print(next(iter(tip)))
#print(tip["o"]["g"]["#"]) next(iter(tip.values()))