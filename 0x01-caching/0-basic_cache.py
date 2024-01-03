#!/usr/bin/env python3

"""Basic Cache"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Cache"""

    def put(self, key, item):
        """add new item to cache"""

        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """get cached item"""
        return self.cache_data.get(key)
