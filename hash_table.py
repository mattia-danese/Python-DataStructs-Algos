"""
DICTIONARY (hash table/map under the hood):
    - uses hash function that converts key to memory address


TIME COMPLEXITY:
    - lookup: O(1)
    - lookup w/ chaining: O(n), same as linked list (if hash function is really bad) 
    - insertion/deletion: O(1)

COLLISION HANDLING:
    - chaining
        - create linked list and chain together all elements with same hash 
    - linear probing
        - sequentially check spots until you find an empty spot

"""

class HashTable:
    def __init__(self):
        self.__MAX = 100
        self.__arr = [[] for i in range(self.__MAX)]

    
    def __get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.__MAX


    def __add(self, key, val):
        h = self.__get_hash(key)

        found = False
        for idx, elem in enumerate(self.__arr[h]):
            if len(elem) == 2 and elem[0] == key:
                self.__arr[h][idx] = (key, val)
                found = True
                break

        if not found:
            self.__arr[h].append((key, val))

    
    def __setitem__(self, key, val):
        self.__add(key, val)


    def __get(self, key):
        h = self.__get_hash(key)

        for k,v in self.__arr[h]:
            if k == key:
                return v

        return None


    def __getitem__(self, key):
        return self.__get(key)


    def delete(self, key):
        h = self.__get_hash(key)

        for idx, elem in enumerate(self.__arr[h]):
            if elem[0] == key:
                del self.__arr[h][idx]


    def __delitem__(self, key):
        self.delete(key)


if __name__ == "__main__":
    hmap = HashTable()
    hmap["ad"] = 10
    hmap["bc"] = 100

    del hmap["bc"]
   
    print(hmap["ad"])
    print(hmap["bc"])
    print(hmap["aa"])
    
