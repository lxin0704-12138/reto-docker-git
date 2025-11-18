from pymongo import MongoClient
from tabulate import tabulate

client = MongoClient("mongodb://root:Lxy20050704.@localhost:27017/")
db = client.coches_mongo

datos = list(db.coches.find({}, {"_id":0}))

headers = ["Marca", "Modelo", "Color", "KM", "Precio"]
rows = [[d["marca"], d["modelo"], d["color"], d["km"], d["precio"]] for d in datos]

print(tabulate(rows, headers=headers, tablefmt="grid"))
