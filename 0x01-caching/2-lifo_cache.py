#!/usr/bin/env python3
""" 2-lifo_cache module """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    class LIFOCache that inherits from BaseCaching
    and is a caching system
    """
    def __init__(self):
        """Initiliaze """
        super().__init__()
        self.queqe = []

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the
        item value for the key key.
        """
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.queqe.pop()
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))

        if key and item:
            self.cache_data[key] = item
            self.queqe.append(key)

    def get(self, key):
        """
        return the value in self.cache_data linked to key.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
