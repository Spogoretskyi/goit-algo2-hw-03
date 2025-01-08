import csv
import timeit
from BTrees.OOBTree import OOBTree


def load_data(file_path):
    items = []
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            item = {
                "ID": int(row["ID"]),
                "Name": row["Name"],
                "Category": row["Category"],
                "Price": float(row["Price"]),
            }
            items.append(item)
    return items


def add_item_to_tree(tree, item):
    tree[item["ID"]] = {
        "Name": item["Name"],
        "Category": item["Category"],
        "Price": item["Price"],
    }


def add_item_to_dict(dictionary, item):
    dictionary[item["ID"]] = {
        "Name": item["Name"],
        "Category": item["Category"],
        "Price": item["Price"],
    }


def range_query_tree(tree, min_price, max_price):
    return [
        value for key, value in tree.items() if min_price <= value["Price"] <= max_price
    ]


def range_query_dict(dictionary, min_price, max_price):
    return [
        value
        for value in dictionary.values()
        if min_price <= value["Price"] <= max_price
    ]


if __name__ == "__main__":
    file_path = "generated_items_data.csv"
    items = load_data(file_path)

    tree = OOBTree()
    dictionary = {}

    for item in items:
        add_item_to_tree(tree, item)
        add_item_to_dict(dictionary, item)

    min_price = 10.0
    max_price = 100.0

    tree_time = timeit.timeit(
        stmt=lambda: range_query_tree(tree, min_price, max_price), number=100
    )

    dict_time = timeit.timeit(
        stmt=lambda: range_query_dict(dictionary, min_price, max_price), number=100
    )

    print(f"Total range_query time for OOBTree: {tree_time:.6f} seconds")
    print(f"Total range_query time for Dict: {dict_time:.6f} seconds")
