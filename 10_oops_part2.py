class Phones:

  def __init__(self, brand, color):
    self.brand = brand
    self.color = color

  def show_config(self):
    print("Color: ", self.color)
    print("Brand: ", self.brand)

class Iphones(Phones):
  def __init__(self, brand, color, model):
    super().__init__(brand, color)
    self.model = model

  def show_config(self):
    super().show_config()
    print("Model: ", self.model)

i = Iphones("Apple", "White", "Iphone 11")
i.show_config()
