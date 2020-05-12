"""Dessert classes."""


class Cupcake:
    """A cupcake."""
    cache = {}

    def __init__(self, name, flavor, price):
      self.name = name
      self.flavor = flavor
      self.price = price
      self.qty = 0
      self.cache[name] = self


    @staticmethod
    def scale_recipe(ingredients, amount):
      scaled_ingredients = []

      for ingredient in ingredients:
        scaled_ingredient = (ingredient[0], ingredient[1]*amount)
        # print(ingredient)
        # print(scaled_ingredient)
        scaled_ingredients.append(scaled_ingredient)

      return scaled_ingredients


    @classmethod
    def get_cupcakes(cls, name):
      if name in cls.cache:
        return cls.cache[name]
      else:
        print("Sorry, that cupcake doesn't exist")


    def add_stock(self, amount):
      self.qty = self.qty + amount


    def sell(self, amount):
      if self.qty == 0:
        print('Sorry, these cupcakes are sold out')
      elif self.qty >= amount:
        self.qty = self.qty - amount
      elif amount > self.qty:
        self.qty = 0
      # else:
      #   print(f"We don't have the amount you want, only have {self.qty} left.")


    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'


if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
