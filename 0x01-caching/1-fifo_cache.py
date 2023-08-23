#!/usr/bin/env python3
""" 1-fifo_cache module """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    class FIFOCache that inherits from BaseCaching
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
        if key and item:
            self.cache_data[key] = item
            self.queqe.append(key)
        else:
            return
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = self.queqe.pop(0)
            del self.cache_data[first_key]
            print("DISCARD: ", first_key)

    def get(self, key):
        """
        return the value in self.cache_data linked to key.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
