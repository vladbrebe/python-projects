from hash_table import HashTable

# The table exposes no __len__, __contains__ or __iter__, so these three
# helpers read its buckets directly. Keeping them here rather than adding
# methods leaves HashTable exactly as written.

def count_entries(table):
    """Total number of key-value pairs across every bucket."""
    return sum(len(bucket) for bucket in table.collection.values())

def all_keys(table):
    """Every key currently stored."""
    return [key for bucket in table.collection.values() for key in bucket]

def all_items(table):
    """Every (key, value) pair currently stored."""
    return [pair for bucket in table.collection.values() for pair in bucket.items()]

def test_add_and_lookup():
    table = HashTable()
    table.add("cat", "a small mammal")
    assert table.lookup("cat") == "a small mammal"

def test_lookup_missing_key_returns_none():
    assert HashTable().lookup("nothing") is None

def test_add_replaces_existing_value():
    table = HashTable()
    table.add("cat", "first")
    table.add("cat", "second")
    assert table.lookup("cat") == "second"
    assert count_entries(table) == 1

def test_anagrams_collide_but_stay_separate():
    # The hash sums character codes, so anagrams share a bucket.
    table = HashTable()
    assert table.hash("listen") == table.hash("silent")

    table.add("listen", "a verb")
    table.add("silent", "an adjective")
    assert table.lookup("listen") == "a verb"
    assert table.lookup("silent") == "an adjective"
    assert len(table.collection) == 1
    assert count_entries(table) == 2

def test_remove_one_key_leaves_its_bucket_mate():
    table = HashTable()
    table.add("listen", "a verb")
    table.add("silent", "an adjective")
    table.remove("listen")
    assert table.lookup("listen") is None
    assert table.lookup("silent") == "an adjective"

def test_remove_missing_key_is_a_no_op():
    table = HashTable()
    table.add("cat", "a small mammal")
    table.remove("dog")
    assert count_entries(table) == 1

def test_remove_leaves_an_empty_bucket_behind():
    # remove() deletes the key but not the bucket, so the bucket count stays
    # at one while the entry count drops to zero.
    table = HashTable()
    table.add("cat", "a small mammal")
    table.remove("cat")
    assert count_entries(table) == 0
    assert len(table.collection) == 1

def test_keys_and_items():
    table = HashTable()
    table.add("cat", 1)
    table.add("dog", 2)
    assert table.lookup("cat") is not None
    assert table.lookup("fish") is None
    assert sorted(all_keys(table)) == ["cat", "dog"]
    assert sorted(all_items(table)) == [("cat", 1), ("dog", 2)]
