def dict_to_list(dataset):
    result = []
    for x in dataset:
        result.append([x, dataset[x]])
    return result

data = {"my_key": "my_value", "your_key": "your_value"}
print(dict_to_list(data))
