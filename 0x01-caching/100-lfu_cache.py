#!/usr/bin/env python3
""" 100-lfu_cache module """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ class LFUCache that inherits from
    BaseCaching and is a caching system """
    def __init__(self):
        """ initialize """
        super().__init__()
        self.freq_counter = {}    # Keeps track of frequency counts
        self.freq_items = {}      # Keeps track of items for each frequency
        self.access_time = {}     # Keeps track of access time for each key
        self.current_time = 0     # Tracks the current time

    def update_frequency(self, key):
        """
        Update the frequency of the given key and move
        it to the new frequency bucket.
        """
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
        """
        Store a new item in the cache.
        """
        if key is None or item is None:
            return

        # If the key already exists, update the value and frequency
        if key in self.cache_data:
            self.cache_data[key] = item
            self.update_frequency(key)
        else:
            # Remove the least frequently used item if the cache is full
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

            # Add the new item and update the frequency
            self.cache_data[key] = item
            self.freq_counter[key] = 1
            if 1 not in self.freq_items:
                self.freq_items[1] = {key}
            else:
                self.freq_items[1].add(key)

        # Update the access time for the key
        if key in self.access_time:
            self.access_time[key] = self.current_time
        else:
            self.access_time[key] = self.current_time
            self.current_time += 1

    def get(self, key):
        """
        Retrieve an item from the cache based on the given key.
        """
        if key is None or key not in self.cache_data:
            return None

        # Update the frequency and access time for the key
        self.update_frequency(key)
        self.access_time[key] = self.current_time
        self.current_time += 1

        return self.cache_data[key]

    def lru(self, items):
        """
        Find the least recently used key among a set of keys.
        """
        lru_key = None
        min_access_time = float('inf')
        for item in items:
            if self.access_time[item] < min_access_time:
                min_access_time = self.access_time[item]
                lru_key = item
        return lru_key
