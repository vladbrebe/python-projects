"""A hash table built on top of separate chaining.

The hash function sums the Unicode code points of the key's characters. That
collides readily (any anagram hashes identically), which is exactly why each
bucket stores a dictionary of the full keys rather than a single value.
"""


class HashTable:
    """
    A data structure that stores key-value pairs
    """
    def __init__(self) -> None:
        self.collection = {}
    
    # Returns the hashed value computed as the sum
    # of the Unicode values of each character in the string
    def hash(self, string: str) -> str:
        return sum([ord(s) for s in string])

    # Takes two arugements and stores them in memory
    def add(self, key: str, value) -> None:
        key_hash  = self.hash(key)

        # Check if exists already
        if key_hash in self.collection:
            self.collection[key_hash][key] = value
        else:
            self.collection[key_hash] = {key: value}

    # Removes a key-value pair corresponding to an existing key
    def remove(self, key: str) -> None:
        key_hash = self.hash(key)

        # Short circuit and to first check existence of hash, and then
        # check existence of exact key
        if key_hash in self.collection and key in self.collection[key_hash]:
            del self.collection[key_hash][key]

    # Returns the value corresponding to the input string
    def lookup(self, key: str):
        key_hash = self.hash(key)
        if key_hash in self.collection and key in self.collection[key_hash]:
            return self.collection[key_hash][key]
        return None


def main() -> None:
    """Demonstrate storage, lookup, collisions and removal."""
    table = HashTable()
    table.add("listen", "a verb")
    table.add("silent", "an adjective")  # Anagram: collides with "listen".
    table.add("cat", "a small mammal")

    entries = sum(len(bucket) for bucket in table.collection.values())
    print(f"Entries: {entries}")
    print(f"'listen' hashes to {table.hash('listen')}")
    print(f"'silent' hashes to {table.hash('silent')} (same bucket)")
    print(f"lookup('listen') -> {table.lookup('listen')}")
    print(f"lookup('silent') -> {table.lookup('silent')}")

    table.remove("cat")
    print(f"After removing 'cat': lookup('cat') -> {table.lookup('cat')}")

    # remove() empties the bucket but leaves it in place, so 312 stays as {}.
    print(f"Buckets: {table.collection}")


if __name__ == "__main__":
    main()