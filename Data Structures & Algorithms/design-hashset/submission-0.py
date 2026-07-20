class MyHashSet:
    def __init__(self):
        # A prime number of buckets to reduce hash collisions
        self.num_buckets = 769
        # Initialize an array where each bucket is a standard Python list
        self.buckets = [[] for _ in range(self.num_buckets)]

    def _get_hash(self, key: int) -> int:
        # Hash function to map key to a bucket index
        return key % self.num_buckets

    def add(self, key: int) -> None:
        index = self._get_hash(key)
        bucket = self.buckets[index]
        
        # Only append if the key isn't already inside this bucket chain
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        index = self._get_hash(key)
        bucket = self.buckets[index]
        
        # If the key exists in the bucket, remove it
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        index = self._get_hash(key)
        bucket = self.buckets[index]
        
        # Returns True if key exists in the specific bucket list
        return key in bucket