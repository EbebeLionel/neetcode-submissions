class MyHashMap:

    def __init__(self):
        self.num_buckets = 769
        self.buckets = [[] for _ in range(self.num_buckets)]

    def _get_hash(self, key: int) -> int:
        return key % self.num_buckets

    def put(self, key: int, value: int) -> None:
        index = self._get_hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def get(self, key: int) -> int:
        index = self._get_hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                if k == key:
                    return v

        return -1

    def remove(self, key: int) -> None:
        index = self._get_hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)