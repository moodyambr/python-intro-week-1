class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_final_price(self):
        return self.price

    def get_extra_label(self):
        return ""

    def get_receipt_line(self):
        extra = self.get_final_price() - self.price

        line = f"{self.__class__.__name__}: {self.name}: {self.price:.2f} kr"

        if extra > 0:
            line += f" + {self.get_extra_label()} {extra:.2f} kr"

        line += f" = {self.get_final_price():.2f} kr"

        return line

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}, price: {self.price} kr"


class Appetizer(MenuItem):
    def __init__(self, name, price, is_glutenfree=False):
        self.name = name
        self.price = price
        self.is_glutenfree = is_glutenfree


class MainCourse(MenuItem):
    def __init__(self, name, price, is_vegetarian=False):
        self.name = name
        self.price = price
        self.is_vegetarian = is_vegetarian

    def get_final_price(self):
        return self.price * 1.15

    def get_extra_label(self):
        return "service fee 15%:"


class Dessert(MenuItem):
    def __init__(self, name, price, is_sweetness=False):
        self.name = name
        self.price = price
        self.is_sweetness = is_sweetness


class Beverage(MenuItem):
    def __init__(self, name, price, is_alcoholic=False):
        self.name = name
        self.price = price
        self.is_alcoholic = is_alcoholic

    def get_final_price(self):
        return self.price * 1.12

    def get_extra_label(self):
        return "drink tax 12%:"


class Order:
    def __init__(self):
        self.ordered_items = []

    def add_item(self, menu_item):
        self.ordered_items.append(menu_item)

    def remove_item(self, menu_item):
        if menu_item in self.ordered_items:
            self.ordered_items.remove(menu_item)

    def calculate_total(self):
        return sum(item.get_final_price() for item in self.ordered_items)


class Table:
    def __init__(self, table_number):
        self.table_number = table_number
        self.current_order = None

    def start_new_order(self):
        self.current_order = Order()

    def close_order(self):
        if self.current_order is None:
            return 0

        total = self.current_order.calculate_total()
        self.current_order = None
        return total


class Restaurant:
    def __init__(self):
        self.menu_items = []
        self.tables = []

    def add_menu_item(self, item):
        self.menu_items.append(item)

    def add_table(self, table):
        self.tables.append(table)

    def get_table(self, table_number):
        for table in self.tables:
            if table.table_number == table_number:
                return table

        raise ValueError(f"Table {table_number} not found.")

    def show_menu(self):
        for item in self.menu_items:
            print(item)

    def assign_table_to_order(self, table_number):
        self.get_table(table_number).start_new_order()

    def process_payment(self, table_number):
        table = self.get_table(table_number)

        if table.current_order is not None:
            print(f"\nThe receipt for table {table_number}:")

            for item in table.current_order.ordered_items:
                print(item.get_receipt_line())

        total = table.close_order()

        print(f"Total payment for table {table_number}: {total:.2f} kr")

        return total

    def run(self):

        self.add_menu_item(Appetizer("Soup", 100))
        self.add_menu_item(MainCourse("Steak", 200))
        self.add_menu_item(Beverage("Beer", 30, is_alcoholic=True))
        self.add_menu_item(Dessert("Waffle", 20, is_sweetness=True))

        self.add_table(Table(1))

        self.assign_table_to_order(1)
    
        table = self.get_table(1)
    
        table.current_order.add_item(self.menu_items[0])
        table.current_order.add_item(self.menu_items[1])
        table.current_order.add_item(self.menu_items[2])
        table.current_order.add_item(self.menu_items[3])
    
        self.process_payment(1)



restaurant = Restaurant()
restaurant.run()