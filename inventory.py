from audioop import maxpp
from cmath import cos
import code
from csv import reader, writer
from gettext import install
from importlib.resources import read_binary
from itertools import product
from tabulate import tabulate

class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def read_data(self):
        try:
            with open("inventory.txt", "r+") as x:
                line = x.readlines()

        except:
            print("Error, no such file.")

shoe_list = []

shoe_list.append(Shoe("South Africa","SKU44386","Air Max 90","2300","20"))
shoe_list.append(Shoe("China","SKU90000","Jordan 1","3200","50"))
shoe_list.append(Shoe("Vietnam","SKU63221","Blazer","1700","19"))
shoe_list.append(Shoe("United States","SKU29077","Cortez","970","60"))
shoe_list.append(Shoe("Russia","SKU89999","Air Force 1","2000","43"))

def search_list(self, code):
    for i in range(len(shoe_list)):
        if shoe_list[i] == code:
            return True
    return False

def __str__(self):
    return "{}"

min_list = []
for obj in shoe_list:
    
    min_list.append(obj.quantity)

max_list = []
for obj in shoe_list:

    max_list.append(obj.quantity)

most_shoes = max(max_list)
least_shoes = min(min_list)

print(most_shoes, obj.product, "needs to go on sale")
print(least_shoes, obj.product, "needs to be restocked")

def value_per_item():
    with open('inventory.txt', 'a+') as file:
        lines = file.readlines()
        file.seek(0,0)
        for line in lines:
            columns = line.strip().split(",")
            file.write(",".join(columns) + ",Value")

def table():
    headers = ['country', 'code', 'product', 'cost', 'quantity']

    country = ['South Africa', 'China', 'Vietnam', 'United States', 'Russia']
    code = ['SKU44386', 'SKU90000', 'SKU63221', 'SKU29077', 'SKU89999']
    product = ['Air Max 90', 'Jordan 1', 'Blazer', 'Cortez', 'Air Force 1']
    cost = [2300, 3200, 1700, 970, 2000]
    quantity = [20, 50, 19, 60, 43]
    shoe = range(1, len(country)+1)

    table = zip(shoe, country, code, product, cost, quantity)
    print(tabulate(table, headers=headers, floatfmt=".4f"))

table()