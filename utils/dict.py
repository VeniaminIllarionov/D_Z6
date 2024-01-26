def get_val(collection, key, default='git'):
    data = collection
    if key in data:
        return data[key]
    return default

print(get_val({'a': 1, 'b': 2}, 'c'))