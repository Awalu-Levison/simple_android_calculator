from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from operations.arithmetic import evaluate_expression
from operations.advanced import square, square_root, percentage
from operations.history import History_Manager

import kivy


class CalculatorLayout(BoxLayout):
    def __init__(self):
        super(CalculatorLayout, self).__init__()
        self.history_manager = History_Manager()

    def calc_symbol(self, symbol):
        self.ids.calc_field.text += symbol
    
    def backspace(self):
        """Clear the screen"""
        self.ids.calc_field.text = self.ids.calc_field.text[:-1]

    def get_result(self):
        """Get result of an operation"""
        expression = self.ids.calc_field.text
        result = evaluate_expression(expression)
        self.ids.calc_field.text = result
        self.history_manager.add_entry(f"{expression} = {result}")
        self.update_history_display()

    def square(self):
        """Find the square of the number"""
        self.ids.calc_field.text = square(self.ids.calc_field.text)
        self.history_manager.add_entry(f"{self.ids.calc_field.text}2")

    def square_root(self):
        """Find square root of a number"""
        self.ids.calc_field.text = square_root(self.ids.calc_field.text)
        self.history_manager.add_entry(f"√{self.ids.calc_field.text}")

    def percentage(self):
        """Calculate percentage of a number"""
        self.ids.calc_field.text = percentage(self.ids.calc_field.text)
        self.history_manager.add_entry(f"{self.ids.calc_field.text}%")

    def clear(self):
        """Clear the screen"""
        self.ids.calc_field.text = ""
    
    def update_history_display(self):
        """Update user data to history list"""
        self.history_data = self.history_manager.get_history()


class FocusCalc(App):
    def build(self):
        return CalculatorLayout()
    
if __name__ == "__main__":
    FocusCalc().run()
