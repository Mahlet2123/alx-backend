#!/usr/bin/env python3
""" 100-lfu_cache module """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    def __init__(self):
        """ initialize """
        super().__init__()
        self.freq_counter = {}  # Keeps track of frequency counts
        self.freq_items = {}    # Keeps track of items for each frequency

    def update_frequency(self, key):
        """ update the frequency for a key """
        frequency = self.freq_counter[key]
        self.freq_items[frequency].remove(key)

        if not self.freq_items[frequency]:
            del self.freq_items[frequency]

        frequency += 1
        self.freq_counter[key] = frequency

        if frequency not in self.freq_items:
            self.freq_items[frequency] = {key}
        else:
            self.freq_items[frequency].add(key)

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.update_frequency(key)
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_frequency = min(self.freq_items)
                items_to_discard = self.freq_items[min_frequency]

                if len(items_to_discard) > 1:
                    lru_key = self.lru(items_to_discard)
                    del self.cache_data[lru_key]
                    items_to_discard.remove(lru_key)
                    self.freq_counter.pop(lru_key)

                discard_key = items_to_discard.pop()
                self.cache_data.pop(discard_key)
                self.freq_counter.pop(discard_key)
                print("DISCARD:", discard_key)

            self.cache_data[key] = item
            self.freq_counter[key] = 1
            if 1 not in self.freq_items:
                self.freq_items[1] = {key}
            else:
                self.freq_items[1].add(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        self.update_frequency(key)
        return self.cache_data[key]

    def lru(self, items):
        """ lru method """
        lru_key = None
        min_access_time = float('inf')
        for item in items:
            if self.access_time[item] < min_access_time:
                min_access_time = self.access_time[item]
                lru_key = item
        return lru_key
