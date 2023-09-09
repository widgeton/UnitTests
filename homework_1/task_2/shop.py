from copy import deepcopy


class Product:
    def __init__(self, cost: int, title: str):
        self._cost = cost
        self._title = title

    @property
    def cost(self):
        return self._cost

    @property
    def title(self):
        return self._title

    def __eq__(self, other):
        return self.cost == other.cost and self.title == other.title

    def __hash__(self):
        return hash((self.cost, self.title))

    def __repr__(self):
        return f"Product({self.cost}, '{self.title}')"


class Shop:
    def __init__(self, products: list[Product]):
        self._products = products

    @property
    def products(self):
        return deepcopy(self._products)

    def sort_products_by_price(self) -> None:
        self._products.sort(key=lambda x: x.cost)

    def get_most_expensive_product(self) -> Product:
        return max(self._products, key=lambda x: x.cost)
