"""
Hash Table implementation for WGUPS Routing Program.
Supports basic insert and lookup operations for package objects.
"""


# HashTable class to manage packages using a simple hashing mechanism
class HashTable:
    def __init__(self, capacity=20):
        """
        Initialize the hash table with a fixed number of empty buckets.

        Args:
            capacity (int): Number of buckets. Default is 20.
        """
        self.table = [[] for _ in range(capacity)]

    def _get_hash(self, key):
        """
        Compute the hash value for a given key.

        Args:
            key: The key to be hashed.

        Returns:
            int: Index for the hash table bucket.
        """
        return hash(key) % len(self.table)

    def insert(self, key, item):
        """
        Insert or update a package in the hash table.

        Args:
            key: Unique key for the package (typically package ID).
            item: The package object to store.

        Returns:
            bool: True if insert/update was successful.
        """
        bucket = self._get_hash(key)
        bucket_list = self.table[bucket]

        for pair in bucket_list:
            if pair[0] == key:
                pair[1] = item
                return True

        bucket_list.append([key, item])
        return True

    def lookup(self, key):
        """
        Look up a package in the hash table by key.

        Args:
            key: Unique key for the package (typically package ID).

        Returns:
            Package: The package object if found, else None.
        """
        bucket = self._get_hash(key)
        bucket_list = self.table[bucket]

        for pair in bucket_list:
            if pair[0] == key:
                return pair[1]
        return None