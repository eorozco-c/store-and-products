from product import Product

class Store:
    def __init__(self,name, products: list[Product] = None):
        self.name = name
        self.products = products or []

    def add_product (self, new_product: Product):
        self.products.append(new_product)
        return self

    def sell_product (self, id: str=None,sku: str=None):
        if sku:
            try:
                id = [p.sku for p in self.products].index(sku)
            except ValueError:
                print(f"SKU: {sku} no fue encontado")
                return self

        if id > len(self.products)-1:
            print("ID de elemento no existe")
            return
        product = self.products.pop(int(id))
        product.print_info()
        return self

    def inflation(self, category,percent_increase):
        for product in filter(lambda p: p.category == category, self.products):
            product.update_price(percent_increase, True)
        return self
    
    def set_clearance(self, category, percent_discount):
        for product in filter(lambda p: p.category == category, self.products):
            product.update_price(percent_discount, False)
        return self


    def inventory(self):
        print(f"Inventario de {self.name}")
        for product in self.products:
            product.print_info()
        return self
