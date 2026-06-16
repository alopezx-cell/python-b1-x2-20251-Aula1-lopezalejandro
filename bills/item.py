from enum import Enum
import datetime
from .entity import *

# Do not change the value of ISD_FACTOR var
ISD_FACTOR = 0.25


class TaxType(Enum):
    # Do not change this enum
    IVA = 1
    ISD = 2


class Tax:
    def __init__(self, tax_id: str, tax_type: TaxType, percentage: float):
        self.tax_id = tax_id
        self.tax_type = tax_type
        self.percentage = percentage


class Product:
    def __init__(self, product_id: str, name: str, expiration_date: datetime, bar_code: str, quantity: int, price: float, taxes: list):
        self.product_id = product_id
        self.name = name
        self.expiration_date = expiration_date
        self.bar_code = bar_code
        self.quantity = quantity
        self.price = price
        self.taxes = taxes

    def calculate_tax(self, tax: Tax) -> float:
        valor = self.quantity * self.price * tax.percentage
        if tax.tax_type == TaxType.ISD:
            valor = valor * ISD_FACTOR
        return valor

    def calculate_total_taxes(self) -> float:
        total = 0
        for tax in self.taxes:
            total += self.calculate_tax(tax)
        return total

    def calculate_total(self) -> float:
        return self.price * self.quantity + self.calculate_total_taxes()

    def __eq__(self, another):
        # Do not change this method
        return hasattr(another, 'product_id') and self.product_id == another.product_id

    def __hash__(self):
        # Do not change this method
        return hash(self.product_id)

    def print(self):
        # Do not change this method
        print(
            f"Product Id:{self.product_id} , name:{self.name}, quantity:{self.quantity}, price:{self.price}")
        for tax in self.taxes:
            print(f"Tax:{tax.tax_type} , percentage:{tax.percentage}")


class Bill:
    def __init__(self, bill_id: str, sale_date: datetime, seller: Seller, buyer: Buyer, products: list[Product]):
        self.bill_id = bill_id
        self.sale_date = sale_date
        self.seller = seller
        self.buyer = buyer
        self.products = products


    def calculate_total(self) -> float:
        total = 0
        for product in self.products:
            total = total + product.calculate_total()
        return total

    def print(self):
        # Do not change this method
        self.buyer.print()
        self.seller.print()
        for product in self.products:
            product.print()