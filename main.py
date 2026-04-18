class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key):
        if key in self.cache:
            value = self.cache[key]
            self.order.remove(key)
            self.order.append(key)
            return value
        else:
            return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache) == self.capacity:
                oldest_key = self.order.pop(0)
                del self.cache[oldest_key]
            self.cache[key] = value
            self.order.append(key)

    def delete(self, key):
        if key in self.cache:
            del self.cache[key]
            self.order.remove(key)

cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))