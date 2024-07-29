import json

d1 = {
    "dummy1": "test",
    "dummy2": "bananão",
    "dummy4": "morango",
    "dummy5": {"foo": "bar", "too": "far", "bar": "vinho"},
    "dummy6": "dummy dummy",
}

d2 = {
    "dummy1": "test",
    "dummy2": "bananinha",
    "dummy3": "BEBES",
    "dummy5": {"bar": "foo"},
    "dummy6": {"bar": "foo"},
}


def recursively_update_dicts(dict_1, dict_2):
    """
    Auxiliary method to recursively update (merge) two dictionaries that might
    have an arbitrary number of nested dictionaries
    """
    updated_dict = dict(dict_1)
    for key, value in dict_2.items():
        # if key in dict_1 and isinstance(dict_1[key], dict) and isinstance(value, dict):
        if key in dict_1 and type(dict_1[key]) is dict and type(value) is dict:
            updated_dict[key] = recursively_update_dicts(dict_1[key], value)
        else:
            updated_dict[key] = value
    return updated_dict


print(json.dumps(recursively_update_dicts(d1, d2), indent=4))
