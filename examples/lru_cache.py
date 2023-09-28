'''
Implement the LRU cache
'''

from time import sleep

class LRUCacheitem(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

class LRUCache(object):

    def __init__(self, length):
        self.length = length
        self.item_list = []
        self.hash = {}

    def insertItem(self, item):

        if item.key in self.hash:
            ind = self.item_list.index(item)
            self.item_list = self.item_list[:ind] + self.item_list[ind + 1:]
            self.item_list.insert(0, item)

            print("Item is moved to position 1")
        else:

            self.item_list.insert(0, item)
            self.hash[item.key] = item
            print("Item is inserted at position 1")


def print_cache(cache):
    for i, item in enumerate(cache.item_list):
        print("index :{0},Key : {1} , Value : {2} ".format(i, item.key, item.value))


if __name__ == "__main__":
    one = LRUCacheitem("sai", "male")
    two = LRUCacheitem("vineesha", "female")
    three = LRUCacheitem("vineel", "male")
    four = LRUCacheitem("adi", "male")

    cache = LRUCache(3)

    cache.insertItem(one)
    cache.insertItem(two)
    cache.insertItem(three)

    print_cache(cache)

    cache.insertItem(one)

    print_cache(cache)

    cache.insertItem(four)

    print_cache(cache)


