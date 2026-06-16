from .entity import *
from .item import *


class OrderType:
    # Do not change this enum
    ASC = 0
    DES = 1


class Statistics:
    def __init__(self, bills: list[Bill]):
        # Do not change this method
        self.bills = bills

    def find_top_sell_product(self) -> (Product, int):
        contador = {}
        for bill in self.bills:
            for product in bill.products:
                if product in contador:
                    contador[product] = contador[product] + 1
                else:
                    contador[product]=1

        top_product = None
        top_count = 0
        for product in contador:
            if contador[product] > top_count:
                top_count = contador[product]
                top_product = product

        return (top_product, top_count)

    def find_top_two_sellers(self) -> list:
        ventas = {}
        for bill in self.bills:
            total = bill.calculate_total()
            if bill.seller in ventas:
                ventas[bill.seller] = ventas[bill.seller] + total
            else:
                ventas[bill.seller] = total

        lista_vendedores = list(ventas.keys())
        lista_vendedores.sort(key=lambda s: ventas[s], reverse=True)

        return lista_vendedores[:2]

    def find_buyer_lowest_total_purchases(self) -> (Buyer, float):
        compras = {}
        for bill in self.bills:
            total = bill.calculate_total()
            if bill.buyer in compras:
                compras[bill.buyer] = compras[bill.buyer] + total
            else:
                compras[bill.buyer] = total

        buyer_menor = None
        menor_total = None
        for buyer in compras:
            if menor_total is None or compras[buyer] < menor_total:
                menor_total = compras[buyer]
                buyer_menor = buyer

        return (buyer_menor, menor_total)

    def order_products_by_tax(self, order_type: OrderType) -> tuple:
        impuestos = {}
        for bill in self.bills:
            for product in bill.products:
                tax_total = product.calculate_total_taxes()
                if product in impuestos:
                    impuestos[product] = impuestos[product] + tax_total
                else:
                    impuestos[product]=tax_total

        lista_productos = list(impuestos.keys())
        if order_type == OrderType.DES:
            lista_productos.sort(key=lambda p: impuestos[p], reverse=True)
        else:
            lista_productos.sort(key=lambda p: impuestos[p])

        resultado = []
        for product in lista_productos:
            resultado.append((product, impuestos[product]))

        return resultado

    def show(self):
        # Do not change this method
        print("Bills")
        for bill in self.bills:
            bill.print()
