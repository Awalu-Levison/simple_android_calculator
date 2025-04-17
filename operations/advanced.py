import math


def square(self):
    # Allow square calculations
    value = self.ids.calc_field.text
    result = square(value)
    self.ids.calc_field.text = result
    self.history_manager.add_entry(f"{value}2 = {result}")
    self.update_history_display()


def square_root(self):
    # calculate square root of numbers
    value = self.ids.calc_field.text
    result = square_root(value)
    self.ids.calc_field.text = result
    self.history_manager.add_entry(f"√{value} = {result}")
    self.update_history_display()



def percentage(number):
    # Convert numbers to percenbtage
    value = self.ids.calc_field.text # type: ignore
    result = percentage(value)
    self.ids.calc_field.text = result # type: ignore
    self.history_manager.add_entry(f"{value}% = {result}") # type: ignore
    self.update_history_display() # type: ignore