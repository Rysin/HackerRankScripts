List1 = [
    {"name": "Jon", "class": 12},
    [{"name": "adam", "class": 5}, {"name": "Sourabh", "class": 15}],
]


def extract_nested_dict_1(_lst):
    for item in _lst:
        if isinstance(item, dict):
            name, age = item.values()
            print(f"My Name is  {name} and class is {age}")
        elif isinstance(item, (list, tuple)):
            return extract_nested_dict_1(item)


if __name__ == "__main__":
    extract_nested_dict_1(List1)
