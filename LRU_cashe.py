from collections import OrderedDict

class Hash:
    od = OrderedDict()
    def __init__(self, size):
        self.size = size

    def get(self, key):
        if key in self.od:
            self.od.move_to_end(key, last=False)
            return self.od[key]
        else:
            return None
    
    def set(self, key, value):
        if len(self.od) == self.size:
            self.od.popitem(last=True)
        self.od[key] = value

h = Hash(2)
h.set("bob", 27)
print(h.get("bob"))
h.set("rob", 45)
print()
print(h.get("bob"))
print(h.get("rob"))
h.set("cob", 7)
print()
print(h.get("bob"))
print(h.get("rob"))
print(h.get("cob"))