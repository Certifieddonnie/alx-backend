#!/usr/bin/env python3
"""
LRU Caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ A Class that inherits from BaseCaching
    and is a caching system
    """
    def __init__(self):
        """ Initializing
        """
        self.mem = []
        super().__init__()

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the item
        value for the key key
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
                if key not in self.mem:
                    self.mem.append(key)
                    #   print(f"1st {self.mem}")
                else:
                    self.mem.remove(key)
                    self.mem.append(key)
                    #    print(f"2nd {self.mem}")
            else:
                if key in self.cache_data:
                    self.cache_data[key] = item
                    self.mem.remove(key)
                    self.mem.append(key)
                    #     print(f"3rd {self.mem}")
                else:
                    lru_key = self.mem[0]
                    del self.cache_data[lru_key]
                    self.cache_data[key] = item
                    self.mem.remove(lru_key)
                    self.mem.append(key)
                    print(f"DISCARD: {lru_key}")
                    #      print(f"4th {self.mem}")

    def get(self, key):
        """ returns the value in self.cache_data
        linked to key
        """
        if key is None or key not in self.cache_data:
            return None

        self.mem.remove(key)
        self.mem.append(key)
        # print(f"5th {self.mem}")

        return self.cache_data[key]
