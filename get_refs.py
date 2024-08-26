import csv

with open("../../../cutelos.csv", "r") as items:
    items_csv = csv.reader(items, delimiter=";")
    ref_items = []
    for item in items_csv:
        print(item)
        if item[3] != '20':
            ref_items.append(item[2])
    print(ref_items)
