def get_val(collection, key, default='git'):
    data = collection
    if key in data:
        return data[key]
    return default

