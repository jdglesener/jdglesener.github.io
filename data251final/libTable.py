#Library implementation for graphs


class LibTable():
    def __init__(self, key = None, val = None):
        self.size = 5000
        self.table = [[] for i in range(self.size)]
        self.keys = [key]
        if val:
            self.table[hash(key)%self.size].append((val,key))
    
    def insert(self, key, val):
        self.keys.append(key)
        if type(key) != list:
            self.table[hash(key)%self.size].append((val,key))
        else:
            self.table[hash(key[0])%self.size].append((val,key))
    
    def get(self, key):
        if type(key) != list:
            ind = hash(key)%self.size
        else:
            ind = hash(key[0])%self.size
        if key in self.keys:
            for i in self.table[ind]:
                if key in i:
                    return i[0]

    def get_keys(self):
        return self.keys

    
    def __repr__(self):
        return str(self.table)
    
    def __str__(self):
        return self.__repr__()

"""new = LibTable("A", "six")
new.insert("B",4)
print(new)
print(new.get("B"))
for i in "CDEFGHIJKLMNOP":
    new.insert(i, i+"A")
print(new)
print(new.get("C"))"""