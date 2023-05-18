#!/usr/bin/env python3
"""
FIFO Caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
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
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """ returns the value in self.cache_data
        linked to key
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
