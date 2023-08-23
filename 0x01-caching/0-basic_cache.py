#!/usr/bin/env python3
""" Basic dictionary """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Implementing basic caching algorithm"""

    def put(self, key, item):
        """inseting data into the cache"""
        if key or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Getting data from the cache"""
        if key:
            return self.cache_data.get(key)
