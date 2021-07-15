from tiendas import Store
from products import Product

store = Store("Tienda FALLAPLEY")
print("#"*20,"Agregando Productos","#"*20)
store.add_product(Product("Celular", 100, "electronic","SKU112233")).add_product(Product("juguete", 10, "juguete","0001122")).add_product(Product("PC", 250, "electronic","ABC1122")).inventory()

print("\n","#"*20,"Reduciendo 50% del precio de categoria 'electronic'","#"*20)
store.set_clearance('electronic', 0.5).inventory()

print("\n","#"*20,"Aumentando 30% del precio de categoria 'juguete'","#"*20)
store.inflation("juguete",0.3).inventory()

print("\n","#"*20,f"eliminando producto por ID 2","#"*20)
store.sell_product(id=2).inventory()

print("\n","#"*20,f"eliminando producto por SKU 0001122","#"*20)
store.sell_product(sku="0001122").inventory()