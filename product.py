class Product:
    def __init__(self,name: str,price,category:str,sku=str()):
        self.name = name
        self.price = price
        self.category = category
        self.sku = sku

    def update_price(self, percent_change, is_increased):
        val_percent = self.price * percent_change
        if is_increased == True:
            self.price += val_percent
            return self
        self.price -= val_percent
        return self
    
    def print_info (self):
        print(f"Nombre producto {self.name}, Categoria: {self.category}, Precio: {self.price}, SKU: {self.sku}")
        return self


