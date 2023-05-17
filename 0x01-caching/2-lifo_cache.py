#!/usr/bin/env python3
"""
LIFO Caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ A Class that inherits from BaseCaching
    and is a caching system
    """
    def __init__(self):
        """ Initializing
        """
        super().__init__()

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the item
        value for the key key
        """
        if key is None or item is None:
            pass

        else:
            if key in self.cache_data:
                del self.cache_data[key]
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = list(self.cache_data.keys())[-2]
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

    def get(self, key):
        """ returns the value in self.cache_data
        linked to key
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
