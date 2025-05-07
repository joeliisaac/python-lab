class CoffeeMenu:
  def __init__(self):
    self.menu = {
      'espresso': 2.50,
      'latte': 2.75,
      'cappuccino': 3.20,
      'americano': 2.70
    }

  def get_price(self,x):
      return self.menu[x]
    
  def add_item(self,x, y):
     self.menu[x] = y
     return self.menu

order = CoffeeMenu()
print(order.get_price('latte'))
print(order.add_item('ice coffe', 3.25))