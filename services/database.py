import duckdb
import pandas as pd

def load_data():
    con = duckdb.connect()

    aisles = pd.read_csv('data/aisles.csv')
    departments = pd.read_csv('data/departments.csv')
    orders = pd.read_csv("data/orders.csv")
    products = pd.read_csv("data/products.csv")
    order_products_prior = pd.read_csv("data/order_products_prior.csv")
    order_products_train = pd.read_csv("data/order_products_train.csv")

    con.register("orders", orders)
    con.register("departments", departments)
    con.register("aisles", aisles)
    con.register("products", products)
    con.register("order_products_prior", order_products_prior)
    con.register("order_products_train", order_products_train)

    return con