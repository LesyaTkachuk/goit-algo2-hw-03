import pandas as pd
import timeit
from BTrees._OOBTree import OOBTree

# define data url
data_url = "./data/generated_items_data.csv"

# read data from url
data = pd.read_csv(
    data_url, encoding="utf-8", delimiter=",", on_bad_lines="skip", index_col=0
)
print(data.head(5))


class DictStore:
    def __init__(self):
        self.store = {}

    def add_item_to_store(self, key, value):
        self.store[key] = value

    def get_item_from_store(self, key):
        return self.store.get(key)

    def remove_item_from_store(self, key):
        del self.store[key]

    def update_item_in_store(self, key, value):
        self.store[key] = value

    def range_query_in_store(self, min_price, max_price):
        result = {}
        for key, value in self.store.items():
            if value["price"] >= min_price and value["price"] <= max_price:
                result[key] = value
        return result


class OOBTreeStore:
    def __init__(self):
        self.store = OOBTree()
        self.store_price = OOBTree()

    def add_item_to_store(self, key, value):
        self.store.update({key: value})
        price = value["price"]
        new_value = value
        new_value["id"] = key
        # create separate tree with price as key for range query
        self.store_price.update({price: new_value})

    def add_item_to_store_price(self, key, value):
        self.store_price.update({key: value})

    def get_item_from_store(self, key):
        return self.store.get(key)

    def remove_item_from_store(self, key):
        del self.store[key]

    def update_item_in_store(self, key, value):
        self.store.update({key: value})

    def range_query_in_store(self, min_price, max_price):
        result = [value for value in self.store_price.values(min_price, max_price)]
        return result


if __name__ == "__main__":
    # initialize dictionary and OOBTree store
    dict_store = DictStore()
    oob_tree_store = OOBTreeStore()

    # fill stores with the data from csv file
    for index, row in data.iterrows():
        dict_store.add_item_to_store(
            index, {column.lower(): row[column] for column in data.columns}
        )
        oob_tree_store.add_item_to_store(
            index, {column.lower(): row[column] for column in data.columns}
        )

    # check some items from the stores
    print("Product ID=88519: ", dict_store.get_item_from_store(88519))
    print("Product ID=73117: ", oob_tree_store.get_item_from_store(73117))

    # compare range queries execution time
    print("=" * 70)
    print(
        f"Range query execution time in DictStore: {timeit.timeit(lambda: dict_store.range_query_in_store(100, 300), number=100)} seconds"
    )
    print(
        f"Range query execution time in OOBTreeStore: {timeit.timeit(lambda: oob_tree_store.range_query_in_store(100, 300), number=100)} seconds"
    )
    print("=" * 70)
